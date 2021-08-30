# spotify-playlist-downloader
Automated downloading tool for Spotify Playlists  
Selenium based tool to download spotify playlists automatically using: 
- `selenium==3.141.0`
- `Spotify-API`
- `spotipy==2.19.0`
- `Youtube Data-API v3`

## Clone
Clone this repository by   
`git clone https://github.com/saadz-khan/spotify-playlist-downloader`
cd to the project by  
`cd spotify-playlist-downloader`

## Dependencies 
For a full list of dependencies check `requirements.txt` file  
Install the dependencies using  
`pip install -r requirements.txt`  

## Prerequisite
- Sign in to the spotify developers dashboard [here](https://developer.spotify.com/dashboard/login) and create, name a project to get the `client_id` and `client_secret`.
- Sign in to the google-api developers console [here](https://console.cloud.google.com/apis)
- Go to `Credential` on the left side-bar and click `Create Credentials` on top of the page then `API key`.
- Edit the `variables.py` file and add the `client_id, client_secret, API key` to `spotify_client_id, spotify_client_secret, youtube_data_api_key` respectively

## Downloading Playlist
Replace spotify-playlist-link with its link by sharing the playlist and copying its link
Run `python main.py spotify-playlist-link` 
