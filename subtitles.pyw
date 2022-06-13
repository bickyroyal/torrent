from app import BaseApp, Movie

# TODO Opensubtitles API: REST or XML-RPC ?


class Subtitles(BaseApp):
    def search(self, query: str) -> dict[str, Movie]:
        pass

    def download(self, movie: Movie) -> bool:
        pass


if __name__ == "__main__":
    Subtitles().mainloop()
