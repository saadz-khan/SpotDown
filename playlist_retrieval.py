from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from sys import argv

def spotify_playlist_info(client_id, client_secret, playlist_id):
	"""This function retrives the track information inside of a playlist
	It inputs client_id and client_secret from spotify dashboard 
	Along with a playlist_id from the link of the playlist. """

	auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
	sp = spotipy.Spotify(auth_manager=auth_manager)

	results = sp.playlist(playlist_id)
	track_list = []

	print("Song - Artist - Album\n")

	for item in results['tracks']['items']:
		track_list.append(item['track']['name'] + ' - ' +
		item['track']['artists'][0]['name'] + ' - ' +
		item['track']['album']['name'])
	print(track_list)
	return track_list
	

spotify_playlist_info(str(argv[1]), str(argv[2]), str(argv[3]))

	# To output a json file from it

"""	for item in results['tracks']['items']:
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

# Append the track dict structure to your results dict structure
result_dict['tracks']['items'].append(track_dict)
out_file = open('track.json','w')
json.dump(result_dict, out_file, indent = 4)"""

