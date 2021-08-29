from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify
import json
from sys import argv

c_id = str(argv[1])
c_secret = str(argv[2])
p_id = str(argv[3])
p_id = p_id[34:]

def spotify_authentication(client_id, client_secret, playlist_id):
	"""
	This part verifies the credentials for the spotify-api usage
	Args:
	client_id:
	client_secret:
	playlist_id: Playlist id in the link of the playlist
	Returns:
	All the data related to the playlists

	"""
	
	auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
	sp = Spotify(auth_manager=auth_manager)
	return sp.playlist(playlist_id)


def spotify_playlist_info(client_id, client_secret, playlist_id):
	"""
	This function retrives the track information inside of a playlist
	It inputs client_id and client_secret from spotify dashboard 
	Along with a playlist_id from the link of the playlist. 
	
	"""

	results = spotify_authentication(client_id, client_secret, playlist_id)
	track_list = []

	#print("Song - Artist - Album\n")
	for item in results['tracks']['items']:
		track_list.append(item['track']['name'] + ' - ' +
		item['track']['artists'][0]['name'] + ' - ' +
		item['track']['album']['name'])
	#print(track_list)
	return track_list
	

def output_json(client_id, client_secret, playlist_id):
	"""
	To output a json file from it

	"""
	results = spotify_authentication(client_id, client_secret, playlist_id)
	# Creating a data structure for json format. 
	result_dict = {
		'tracks': {
			'items': [],
			'limit': 100,
			'next': None,
			'offset': 0,
			'previous': None,
			'total': 16
			},
			'type': 'playlist',
			'uri': p_id
			}

	for item in results['tracks']['items']:
		track_dict = {
			'track': {
			'album': {
				'name': item['track']['album']['name'],
			},
			'artists': [{
				'name': item['track']['artists'][0]['name'],
			}],
			'name': item['track']['name'],
			}
		}
		result_dict['tracks']['items'].append(track_dict)

	# Append the track dict structure to your results dict structure
	
	out_file = open('track.json','w')
	json.dump(result_dict, out_file, indent = 4)

# Sample Script 
# spotify_playlist_info(c_id, c_secret, p_id)