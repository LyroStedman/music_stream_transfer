# How to Deezer2Spotify

This program lists all your favorite tracks in Deezer and transfer them into Spotify.

It downloads all metadata from Deezer for your favoritetracks playlist.
Then, for each track,it searches in Spotify if the track exists by looking for its **name**, **artist** and **album**.
If a track is not found it is added to a list.

After every track is covered, all the not found tracks present in the list are searched again in Spotify, but this time, only by looking for their **name** and **artist**.

Ay missing track after that is not searched again and added in a file created to list them.

## Librairies

This program uses a python librairy named Spotipy to ease authentication on Spotify.

## Configuration

You will need to provide your user ID, which can be found by login into Deezer and check the url where you are transferred when you go to https://www.deezer.com/fr/profile/me.
Enter this ID into the config.yaml file.

In contrary to Deezer, Spotify is kinda strict on security (good for them). In order to use the app, you will need to declare an app on your profile.
This can be done on the Dashboard at this address when you log in whith your classic Spotify account : https://developer.spotify.com/dashboard/login

On the dashboard, create an app with whatever name you want and report the client ID and client secret into the config.yaml file.

## Imports

The program is ready to launch, but maybe not your system.

Be sure you have the following dependencies on your system :
Python3
PyYaml
Spotipy (pip install spotipy --upgrade)

## Launch

One everything is ready, you can launch the program with the following line :
python3 [installation_folder]/transferPlaylistTracks.py

## Retrieve tracks that are not found in Spotify

If after the two passes, there are still tracks that are not foudn (usually tracks with special characters), a file named *transfer_failures.txt* is created for you to manually add any missing track.
