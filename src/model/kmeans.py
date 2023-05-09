import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

normalized_df = pd.read_csv("../../data/dataset_normalizzato.csv")

##alcuni grafici che rappresentano i brani con le features più alte e più basse nel dataset.
orderedDf = normalized_df.sort_values(by = ['danceability'], ascending = False, ignore_index=True)
dfToPlot = orderedDf.head(5)
ax = dfToPlot.plot(title = 'Danceability', x = 'titolo', y = 'danceability', legend = False, kind = "barh", color='red')
ax.get_figure().tight_layout()
plt.savefig("../../grafici/danceability.png")

orderedDf = normalized_df.sort_values(by = ['energy'], ascending = False, ignore_index=True)
dfToPlot = orderedDf.head(5)
ax = dfToPlot.plot(title = 'Energy', x = 'titolo', y = 'danceability', legend = False, kind = "barh", color='cyan')
ax.get_figure().set_in_layout(True)
plt.savefig("../../grafici/energy.png")

orderedDf = normalized_df.sort_values(by = ['liveness'], ascending = False, ignore_index=True)
dfToPlot = orderedDf.head(5)
ax = dfToPlot.plot(title = 'liveness', x = 'titolo', y = 'danceability', legend = False, kind = "barh", color='green')
ax.get_figure().set_in_layout(True)
plt.savefig("../../grafici/liveness.png")

curva = []
K = range(2,10)
normalized_df.drop('titolo', axis=1, inplace=True)
for k in K:
    kmeanModel = KMeans(n_clusters=k, n_init=10)
    kmeanModel.fit(normalized_df)
    curva.append(kmeanModel.inertia_)

plt.figure(figsize=(16,8))
plt.plot(K, curva)
plt.xlabel('Numero di Cluster (k)')
plt.ylabel('SSE')
plt.title('Il metodo Elbow Point mostra il k ottimale per il clustering.')
plt.show()

##realizzazione del PCA a 2 dimensioni
pca = PCA(2)
df_train = pca.fit_transform(normalized_df)
print("debug 1")

##applicazione del kMeans.
kmeans = KMeans(5, n_init=10, max_iter=100)
assigned_clusters = kmeans.fit_predict(df_train) ##fase di training
print("Cluster creati")
print(assigned_clusters)
print(df_train)

##plot dei risultati
filtered_label0 = df_train[assigned_clusters == 0]
filtered_label1 = df_train[assigned_clusters == 1]
filtered_label2 = df_train[assigned_clusters == 2]
filtered_label3 = df_train[assigned_clusters == 3]
filtered_label4 = df_train[assigned_clusters == 4]
centroids = kmeans.cluster_centers_
plt.xlabel('PrincipalComponent1')
plt.ylabel('PrincipalComponent2')
plt.title('Rappresentazione dei cluster (kMeans)')
plt.scatter(filtered_label0[:,0] , filtered_label0[:,1] , color = 'red')
plt.scatter(filtered_label1[:,0] , filtered_label1[:,1] , color = 'limegreen')
plt.scatter(filtered_label2[:,0] , filtered_label2[:,1] , color = 'fuchsia')
plt.scatter(filtered_label3[:,0] , filtered_label3[:,1] , color = 'dodgerblue')
plt.scatter(filtered_label4[:,0] , filtered_label4[:,1] , color = 'orange')
plt.scatter(centroids[:,0], centroids[:,1], marker = "*", zorder = 10, c=['yellow', 'yellow','yellow', 'yellow', 'yellow'])
plt.show()
