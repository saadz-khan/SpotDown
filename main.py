from spotipy_client.client import spotify_playlist_info
from google_data_client.client import youtubeSearch, getURL
from downloader import download_multiple_song
from variables import *
import sys

# Sample Script
# python main.py client_id client_secret playlist_link youtube_dev_key

playlist_link = str(sys.argv[1])
client_id = spotify_client_id
client_secret = spotify_client_secret
youtube_key = youtube_data_api_key
playlist_id = playlist_link[34:]

tracks = spotify_playlist_info(client_id, client_secret, playlist_id)

urls = []
for track in tracks:
	response = youtubeSearch(track, youtube_key)
	urls.append(getURL(response))

download_multiple_song(urls)