import pandas as pd
import plotly.express as px
import os

def plot_photos_by_weather(df_trips):
# Chargement du document cible

  df_trips = pd.read_csv('clean_data.csv')

  # Sélection des éléments du dataframe souhaités (Nombre de photos moyen selon la météo)
  # reset_index() pour convertir de la serie en dataframe utilisable avec ploty
  nb_photos_weather = df_trips.groupby('weather')['photos'].mean().reset_index()


  # Génération d'un graphique en barres pour la répartition du nombre de photos moyen selon la météo
  fig = px.bar(nb_photos_weather, x='photos', y='weather',
                title='Nombre moyen de photos selon la météo',
                labels={'photos': 'Photos', 'weather': 'Météo' })

  fig.write_html("graph.html", auto_open=False)
  os.system('powershell.exe start graph.html')

def plot_mood_distribution(df_trips):
  # Génération d'un graphique de répartition des humeurs
  df_trips = pd.read_csv('clean_data.csv')
  # Comptage des humeurs
  repartition_humeur = df_trips['mood'].value_counts().reset_index()
  # Nommage des colonnes adaptées à plotly
  repartition_humeur.columns = ['mood', 'count']

  fig = px.pie(repartition_humeur, names='mood', values='count',
              title='Répartition des humeurs',
              labels={'mood': 'Humeurs'}
              )

  fig.write_html("graph.html", auto_open=False)
  os.system('powershell.exe start graph.html')

def plot_photo_by_date(df_trips):
  # Visualisation des photos prises dans le temps
  df_trips = pd.read_csv('clean_data.csv')
  # Conversion des dates en datetime
  df_trips['date'] = pd.to_datetime(df_trips['date'])
  # Selection des dates
  df_trips = df_trips.sort_values('date')

  fig = px.line(df_trips, x='date', y='photos', color='weather',
                title='Nombre de photos par date',
                labels={'date': 'Date', 'photos': 'Nombre de photos'}
              )

  fig.write_html("graph.html", auto_open=False)
  os.system('powershell.exe start graph.html')
