# SpotDown
> Automated downloading tool for Spotify playlists.  

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![selenium](https://img.shields.io/badge/Selenium-3.141.0-blue)](https://www.selenium.dev/selenium/docs/api/py/api.html)
[![spotipy](https://img.shields.io/badge/Spotipy-2.19.0-blue)](https://spotipy.readthedocs.io/en/2.19.0/)
[![google-data-API](https://img.shields.io/badge/Google%20data--API-v3-blue)](https://developers.google.com/youtube/v3)
[![dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)]()

Selenium based tool to download spotify playlists automatically using: 
- `Python 3.7-3.8 (tested)`
- `selenium==3.141.0`
- `Spotify-API`
- `spotipy==2.19.0`
- `Youtube Data-API v3`

## Table of content

- [Installation](#installation)
    - [Cloning](#cloning)
    - [Create Virtual Environment](#create-virtual-environment)
    - [Activate Virtual Environment](#activate-virtual-environment)
    - [Dependency Installation](#dependency-installation)
    - [Install Chrome Webdriver](#install-chrome-webdriver)
    - [Prerequisite](#prerequisite)
    - [Download Playlist](#download-playlist)
- [Contribute](#contribute)
- [License](#license)


## Problem
## Dependencies 
For a full list of dependencies check `requirements.txt`.  

# Installation
## Windows

## Cloning
Clone this repository `git clone https://github.com/saadz-khan/SpotDown`  
  
## Create Virtual Environment
- Change your current working directory by `cd SpotDown`
- Create virutal environment using `python -m venv env`

## Activate Virtual Environment
To activate the virtual  environment run:
- `env\Scripts\activate.bat` for `Command Prompt`  

- `env\Scripts\activate` in `Windows Powershell`  

## Dependency Installation
Install the dependencies using `pip install -r requirements.txt`  
  
  
## Install Chrome Webdriver
- Install webdriver from this [link](https://chromedriver.chromium.org/downloads/)  
  
<p align="center">
  <img src="https://media.giphy.com/media/bMTzxmMmF6dyG2CSTL/source.gif?cid=790b7611dbd64a5860c863f445f0e33b05d6a4aaa530cad9&rid=source.gif" alt="animated-gif1" />
</p>  
    
-Unzip the file to the `SpotDown/SpotDown`  
## Prerequisite
**This part is a one time setup. Note down your API-keys and keep them to yourself** 
- Sign in to the spotify developers dashboard [here](https://developer.spotify.com/dashboard/login) and create, name a project to get the `client_id` and `client_secret`.  
**Demo below (client_keys generated below is deleted)**

<p align="center">
  <img src="https://media.giphy.com/media/FK5eKB1zFLqy9nHrjL/source.gif?cid=790b76110e1b23f7d2695c3cc54a8b53bd7a00132d32f223&rid=source.gif" alt="animated-gif2" />
</p>  
  
- Sign in to the google-api developers console [here](https://console.cloud.google.com/apis).
- Go to the `Library` and search `Youtube Data API v3` and click `Enable this API`.
- Go to `Credential` on the left side-bar and click `Create Credentials` on top of the page then `API key`.  
**Demo for above 3 steps below (API_Key generated below is deleted)**  

<p align="center">
  <img src="https://media.giphy.com/media/K0oA6mXUDFOjl5iTKH/source.gif?cid=790b7611b01d6ae6d23240007e5eb47e5c8419c25e35bd87&rid=source.gif" alt="animated-gif3" />
</p>    

- Edit the `variables.py` file and add the `client_id, client_secret, API key` to `spotify_client_id, spotify_client_secret, youtube_data_api_key` respectively.

## Download Playlist
Replace `https://open.spotify.com/playlist/link_to_playlist` with actual link by sharing the playlist and copying its link and Run:  
```
python main.py https://open.spotify.com/playlist/link_to_playlist

```  
  
## Contribute
Contributions, issues and feature requests are welcome.
Feel free to check issues page if you want to contribute.
Check the [contributing guide](https://github.com/saadz-khan/SpotDown/blob/master/CONTRIBUTING.md).

## License
Copyright (c) 2021 [Saad Zafar Khan](https://github.com/saadz-khan)  
This project is [MIT](https://github.com/saadz-khan/SpotDown/blob/master/LICENSE) licensed.   

    
## End Note
> Enjoy! A star would be appreciated. Issues and Pull Requests are open.  
> Happy developing!
