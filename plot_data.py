import pandas as pd
import plotly.express as px

# Chargement du document cible

df_trips = pd.read_csv('clean_data_exo4.csv')

# Sélection des éléments du dataframe souhaités (Nombre de photos moyen selon la météo)
# reset_index() pour convertir de la serie en dataframe utilisable avec ploty
nb_photos_weather = df_trips.groupby('weather')['photos'].mean().reset_index()


# Génération d'un graphique en barres pour la répartition du nombre de photos moyen selon la météo
fig = px.bar(nb_photos_weather, x='photos', y='weather',
              title='Nombre moyen de photos selon la météo',
              labels={'photos': 'Photos', 'weather': 'Météo' })

fig.show()

# Génération d'un graphique de répartition des humeurs

# Comptage des humeurs
repartition_humeur = df_trips['mood'].value_counts().reset_index()
# Nommage des colonnes adaptées à plotly
repartition_humeur.columns = ['mood', 'count']

fig = px.pie(repartition_humeur, names='mood', values='count',
             title='Répartition des humeurs',
             labels={'mood': 'Humeurs'}
             )

fig.show()

# Visualisation des photos prises dans le temps
# Comptage des photos
evolution_photos = df_trips['photos'].value_counts
# Conversion des dates en datetime
df_trips['date'] = pd.to_datetime(df_trips['date'])
# Selection des dates
df_trips = df_trips.sort_values('date')

fig = px.line(df_trips, x='date', y='photos', color='weather',
              title='Nombre de photos par date',
              labels={'date': 'Date', 'photos': 'Nombre de photos'}
            )

fig.show()