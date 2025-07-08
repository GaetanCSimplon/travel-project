import pandas as pd

def print_statistics(filename):
    df_trips = pd.read_csv(filename)
    # Affichage distribution valeur météo et humeur
    show_weather_mood = df_trips[['weather', 'mood']]
    print(show_weather_mood)
    # Affichage moyenne des photos
    show_average_photo = df_trips['photos'].mean()
    print('Le nombre de photo moyen est de ', show_average_photo)
    # Affichage médiane
    show_mediane_photo = df_trips['photos'].median()
    print('La médiane est de ', show_mediane_photo)
    # Affichage min
    show_min_photo = df_trips['photos'].min()
    print('Le nombre minimum de photo prise est de ', show_min_photo)
    # Affichage max
    show_max_photo = df_trips['photos'].max()
    print('Le nombre maximum de photo prise est de ', show_max_photo)
    # Affichage du nombre de valeur manquante
    show_missing = df_trips.isna().sum()
    print(show_missing)
    # Affichage du nombre de valeur num erronée
    show_error = df_trips['photos'].fillna(0)
    print(show_error)

