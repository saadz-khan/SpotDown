from playlist_retrieval import spotify_playlist_info
from youtube_search import youtubeSearch, getURL
from downloader import download_multiple_song
import sys


client_id = str(sys.argv[1])
client_secret = str(sys.argv[2])
playlist_link = str(sys.argv[3])
youtube_key = sys.argv[4]
playlist_id = playlist_link[34:]

tracks = spotify_playlist_info(client_id, client_secret, playlist_id)

urls = []
for track in tracks:
	response = youtubeSearch(track, youtube_key)
	urls.append(getURL(response))

download_multiple_song(urls)