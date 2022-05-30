from app import BaseApp, Movie
import requests

class Torrent(BaseApp):
    def search(self, query: str) -> dict[str, Movie]:
        try:
            url = f"https://yts.torrentbay.to/api/v2/list_movies.json?query_term={query}&sort_by=rating"
            movies = requests.get(url).json()["data"]["movies"]
        except KeyError:
            return {}
        return {str(movie["id"]): movie for movie in movies if movie["torrents"]}
    
    def download(self, movie: Movie) -> bool:
        torrent = sorted(movie["torrents"], key=lambda t: (t["type"] == "bluray", t["quality"] == "1080p"))[-1]       
        filename = f"{movie['slug']}.torrent"
        data = requests.get(torrent["url"]).content
        with open(filename, "wb") as outfile:
            return bool(outfile.write(data))


if __name__ == "__main__":
    Torrent().mainloop()
