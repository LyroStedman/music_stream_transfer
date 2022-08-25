% How to Deezer2Spotify

This program lists all your favorite tracks in Deezer and transfer them into Spotify.

# Librairies

This program uses a python librairy named Spotipy to ease authentication on Spotify.

# Configuration

You will need to provide your user ID, which can be found by login into Deezer and check the url where you are transferred when you go to https://www.deezer.com/fr/profile/me.
Enter this ID into the config.yaml file.

In contrary to Deezer, Spotify is kinda strict on security (good for them). In order to use the app, you will need to declare an app on your profile.
This can be done on the Dashboard at this address when you log in whith your classic Spotify account : https://developer.spotify.com/dashboard/login

On the dashboard, create an app with whatever name you want and report the client ID and client secret into the config.yaml file.

# Imports

The program is ready to launch, but maybe not your system.

Be sure you have the following dependencies on your system :
Python3
PyYaml
Spotipy (pip install spotipy --upgrade)

# Launch

One everything is ready, you can launch the program with the following line :
python3 [installation_folder]/transferPlaylistTracks.py