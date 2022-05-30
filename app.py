from abc import ABC, abstractmethod
from typing import TypedDict
from tkinter import Tk, ttk
from tkinter.constants import *


class Movie(TypedDict):
    title: str
    year: int


class BaseApp(ABC, Tk):
    _movies: dict[str, Movie] = {}
    
    @abstractmethod
    def search(self, query: str) -> dict[str, Movie]:
        pass

    @abstractmethod
    def download(self, movie: Movie) -> bool:
        pass

    def __init__(self):
        Tk.__init__(self)
        self.minsize(300, 240)
        self.title(self.__class__.__name__)

        self._searchbar = ttk.Entry(self)
        self._searchbar.pack(fill=X, expand=True, padx=8, pady=8)

        self._tree = ttk.Treeview(self, columns=("title", "year"), show="tree", selectmode="browse")
        self._tree.pack(fill=BOTH, expand=True, padx=8, pady=(0, 8))
        self._tree.column("#0", width=0, stretch=False)
        self._tree.column("year", width=64, stretch=False, anchor=CENTER)

        self._searchbar.bind("<Return>", self._search)
        self._searchbar.bind("<Escape>", lambda e: self.destroy())
        self._tree.bind("<Return>", self._download)
        self._tree.bind("<Escape>", lambda e: self._searchbar.focus_set())

        self._searchbar.focus_set()

    def _search(self, _):
        self._movies = self.search(self._searchbar.get())

        self._tree.delete(*self._tree.get_children())
        for iid, movie in self._movies.items():
            self._tree.insert("", END, iid, values=(movie["title"], movie["year"]))

        if self._movies:
            child = self._tree.get_children()[0]
            self._tree.focus(child)
            self._tree.selection_set(child)
            self._tree.focus_set()
        else:
            self._searchbar.select_range(0, END)
            self._searchbar.focus_set()
    
    def _download(self, _):
        try:
            selected = self._tree.selection()[0]
            movie = self._movies[selected]
        except (KeyError, IndexError) as e:
            return
        if self.download(movie):
            self.destroy()
