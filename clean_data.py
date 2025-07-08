import pandas as pd

# Création d'une fonction 
def load_and_clean_data(filename, new_filename):
    # Récupération du csv
    clean_data = pd.read_csv(filename)
    # Remplacement des valeurs manquantes
    clean_data = clean_data.fillna('unknown')

    # Présence d'une valeur négative dans les photos
    # Utilisation de la fonction where() pour localiser et changer les valeurs négatives et les mettre à 0
    # L'alternative à cette méthode serait d'interpréter les valeurs négatives comme une erreur de saisie et
    # de ramener ces valeurs en positif
    clean_data['photos'] = clean_data['photos'].where(clean_data['photos'] > 0, 0)

    # Conversion au format datetime
    clean_data['date'] = pd.to_datetime(clean_data['date'])

    clean_data.to_csv(new_filename, index=False)
    return clean_data



