# Spotify Playlist Downloader
> Automated downloading tool for Spotify playlists.  

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![selenium](https://img.shields.io/badge/Selenium-3.141.0-blue)](https://www.selenium.dev/selenium/docs/api/py/api.html)
[![spotipy](https://img.shields.io/badge/Spotipy-2.19.0-blue)](https://spotipy.readthedocs.io/en/2.19.0/)
[![google-data-API](https://img.shields.io/badge/Google%20data--API-v3-blue)](https://developers.google.com/youtube/v3)
[![dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)]()

Selenium based tool to download spotify playlists automatically using: 
- `selenium==3.141.0`
- `Spotify-API`
- `spotipy==2.19.0`
- `Youtube Data-API v3`

## Dependencies 
For full list of dependencies check `requirements.txt`.  

# Installation Steps
## Windows

## 1. Cloning
Clone this repository `git clone https://github.com/saadz-khan/spotify-playlist-downloader`  

## 2. Create Virtual Environment
- Change your current working directory by `cd spotify-playlist-downloader`
- Create virutal environment using `python -m venv env`

## 3. Activate Virtual Environment
To activate the virtual  environment run:
- `env\Scripts\activate.bat` for `Command Prompt` 
                      OR
- `env\Scripts\activate` in `Windows Powershell`

## 4. Dependency Installation
3. Install the dependencies using `pip install -r requirements.txt`  

## 5. Prerequisite
4. Sign in to the spotify developers dashboard [here](https://developer.spotify.com/dashboard/login) and create, name a project to get the `client_id` and `client_secret`.
5. Sign in to the google-api developers console [here](https://console.cloud.google.com/apis)
6. Go to `Credential` on the left side-bar and click `Create Credentials` on top of the page then `API key`.
7. Edit the `variables.py` file and add the `client_id, client_secret, API key` to `spotify_client_id, spotify_client_secret, youtube_data_api_key` respectively

## 6. Downloading Playlist
8. Replace `https://open.spotify.com/playlist/link_to_playlist` with actual link by sharing the playlist and copying its link and Run:  
```
python main.py https://open.spotify.com/playlist/link_to_playlist

```
