# spotify-playlist-downloader
Automated downloading tool for Spotify playlists.  
Selenium based tool to download spotify playlists automatically using: 
- `selenium==3.141.0`
- `Spotify-API`
- `spotipy==2.19.0`
- `Youtube Data-API v3`

## Dependencies 
For full list of dependencies check `requirements.txt`.  

## Clone
1. Clone this repository by `git clone https://github.com/saadz-khan/spotify-playlist-downloader`  
2.  Change your current working directory by `cd spotify-playlist-downloader`

## Dependency Installation
3. Install the dependencies using `pip install -r requirements.txt`  

## Prerequisite
4. Sign in to the spotify developers dashboard [here](https://developer.spotify.com/dashboard/login) and create, name a project to get the `client_id` and `client_secret`.
5. Sign in to the google-api developers console [here](https://console.cloud.google.com/apis)
6. Go to `Credential` on the left side-bar and click `Create Credentials` on top of the page then `API key`.
7. Edit the `variables.py` file and add the `client_id, client_secret, API key` to `spotify_client_id, spotify_client_secret, youtube_data_api_key` respectively

## Downloading Playlist
8. Replace `https://open.spotify.com/playlist/link_to_playlist` with actual link by sharing the playlist and copying its link and Run:  
```
python main.py https://open.spotify.com/playlist/link_to_playlist

```
