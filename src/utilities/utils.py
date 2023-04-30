
import spotipy
from spotipy import SpotifyOAuth
import cfg
import pandas as pd
import numpy as np
import csv


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = cfg.SPOTIPY_CLIENT_ID, 
                         client_secret =  cfg.SPOTIPY_CLIENT_SECRET, 
                         redirect_uri= cfg.SPOTIPY_REDIRECT_URI, 
                         scope= cfg.SCOPE, 
                         requests_timeout=10))

"""
    crea una lista con gli id delle canzoni
"""
def get_fav_tracks_list():
    offset = 0
    tracce = []

    while True:
        response = sp.current_user_saved_tracks(
                                 offset=offset,
                                 limit=50)

        if(len(response['items']) == 0):
            break

        for item in response['items']:
            tracce.append(item["track"]["id"])

        offset = offset + len(response['items'])

    return tracce

def create_dataset():
    tracce_id = get_fav_tracks_list()
    features_values = []
    features_names = ['danceability', 'energy', 'valence', 'acousticness', 
                      'speechiness', 'instrumentalness', 'liveness', 'tempo', 'id']

    for song in tracce_id:
        idx = tracce_id.index(song)
        song_array = list([sp.audio_features(song)[0][features_names[0]], 
                              sp.audio_features(song)[0][features_names[1]], 
                              sp.audio_features(song)[0][features_names[2]], 
                              sp.audio_features(song)[0][features_names[3]], 
                              sp.audio_features(song)[0][features_names[4]],
                              sp.audio_features(song)[0][features_names[5]],
                              sp.audio_features(song)[0][features_names[6]],
                              sp.audio_features(song)[0][features_names[7]],
                              tracce_id[idx]]
                              )
        
        features_values.append(song_array)

    with open('../../data/dataset.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(features_names)
        writer.writerows(features_values)
        

create_dataset()

    

