import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

dataset = pd.read_csv("../../data/dataset.csv", sep=',')
istogramma = dataset[['danceability', 'energy', 'valence', 'acousticness', 
                      'speechiness', 'instrumentalness', 'liveness', 'tempo']]
dataset.hist(figsize=(10, 8))
plt.savefig("istogrammaDataset.png")

"""
    Funzione di preprocessing
        - feature selection
        - normalizzazione dei dati
"""
def pre(data):
    to_drop_columns = ['id']
    colonne_tenute = ['danceability', 'energy', 'valence', 'acousticness', 
                      'speechiness', 'instrumentalness', 'liveness', 'tempo', 'titolo']

    data.drop(to_drop_columns, axis=1, inplace=True)
    scaler = preprocessing.MinMaxScaler((0, 1))
    scaler.fit_transform(data[['danceability', 'energy', 'valence', 'acousticness', 'speechiness', 'instrumentalness', 'liveness', 'tempo']])
    #data = scaler.fit_transform(dataset)
    data = pd.DataFrame(data=data, columns=colonne_tenute)

    data.hist(figsize=(10,8))
    plt.savefig("dataset_normalizzato.png")

    data.to_csv(sep=',', path_or_buf='../../data/dataset_normalizzato.csv', index=False)
    return

pre(dataset)
