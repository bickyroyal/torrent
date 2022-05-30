from app import BaseApp, Movie

class Subtitles(BaseApp):
    def search(self, query: str) -> dict[str, Movie]:
        """ TODO """

    def download(self, movie: Movie) -> bool:
        """ TODO """


if __name__ == "__main__":
    Subtitles().mainloop()
