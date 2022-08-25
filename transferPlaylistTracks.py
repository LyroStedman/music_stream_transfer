import requests
import json
import spotipy
import yaml
import base64
from spotipy.oauth2 import SpotifyOAuth


def transfer_failure(search_response, track):
    print(search_response)
    not_found_tracks.append(track)


def get_next_tracks_page(playlist_tracks):
    next_page_url = playlist_tracks["next"]
    playlist_tracks.pop("next")
    return requests.get(next_page_url).json()


def add_to_liked_tracks(playlist_tracks):
    for track in playlist_tracks["data"]:
        track_name = track["title"]
        track_artist = track["artist"]["name"]
        track_album = ""
        if "album" in track:
            track_album = track["album"]["title"]
        if track_album != "":
            search_query = "track:" + track_name + "+artist:" + track_artist + "+album:" + track_album
        else:
            search_query = "track:" + track_name + "+artist:" + track_artist
        print(search_query)
        search_response = json.loads(requests.get("https://api.spotify.com/v1/search?q=" + search_query,
                                                  params={"type": "track"},
                                                  headers={"Authorization": authentication_client,
                                                           "Content-Type": "application/json"}).text)
        if "tracks" in search_response:
            searched_tracks = search_response["tracks"]
            print(searched_tracks["href"])
            print()
            if searched_tracks["total"] > 0:
                searched_track_id = searched_tracks["items"][0]["id"]
                print(searched_track_id)
                sp.current_user_saved_tracks_add(tracks=[searched_track_id])
            else:
                transfer_failure(search_response, track)
        else:
            transfer_failure(search_response, track)
    if "next" in playlist_tracks:
        add_to_liked_tracks(get_next_tracks_page(playlist_tracks))


with open('config.yaml') as file:
    try:
        authentication_config = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)
client_id = authentication_config["authentication"]["client_id"]
client_secret = authentication_config["authentication"]["client_secret"]
basic_credentials = base64.b64encode(bytes(client_id + ":" + client_secret, 'utf-8')).decode()
auth_response = requests.post("https://accounts.spotify.com/api/token", data="grant_type=client_credentials", headers={
    "Authorization": "Basic " + basic_credentials,
    "Content-Type": "application/x-www-form-urlencoded"})
token = json.loads(auth_response.text)
authentication_client = token["token_type"] + " " + token["access_token"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               scope="user-library-modify",
                                               redirect_uri="http://localhost:8000/callback"))
not_found_tracks = []
add_to_liked_tracks(requests.get("https://api.deezer.com/user/" + str(authentication_config["deezer"]["user_id"]) + "/tracks").json())
for not_found_track in not_found_tracks:
    not_found_track.pop("album")
retry_not_found_tracks = not_found_tracks.copy()
tracks_to_retry = {"data": retry_not_found_tracks}
not_found_tracks.clear()

add_to_liked_tracks(tracks_to_retry)
print(not_found_tracks)
f = open("transfer_failures.txt", "w")
for not_found_track in not_found_tracks:
    f.write(not_found_track)
f.close()
