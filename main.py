import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

from add_data import (
    demander_ajout_voyage,
    demander_nb_photos,
    add_data
)
from clean_data import load_and_clean_data
from print_stat import print_statistics
from plot_data import (
    plot_mood_distribution,
    plot_photo_by_date,
    plot_photos_by_weather
)

def main():
    voyages = []
    # Extraction des données vers une liste
    while demander_ajout_voyage():
        voyage = add_data()
        voyages.append(voyage)
    if voyages:
        df = pd.DataFrame(voyages)
        df.to_csv('nouveau_voyage.csv', index=False)
        print('Nouveau voyage ajouté.')
    clean_data = load_and_clean_data('nouveau_voyage.csv', 'clean_data.csv')
    print_statistics('clean_data.csv')
    plot_photos_by_weather(clean_data)
    plot_mood_distribution(clean_data)
    plot_photo_by_date(clean_data)

if __name__ == '__main__':

    main()
