import pandas as pd

clean_data = pd.read_csv('travel_data.csv')
# Remplacement des valeurs manquantes
clean_data.fillna('unknown')

# Présence d'une valeur négative dans les photos
# Utilisation de la fonction where() pour localiser et changer les valeurs négatives et les mettre à 0
# L'alternative à cette méthode serait d'interpréter les valeurs négatives comme une erreur de saisie et
# de ramener ces valeurs en positif
clean_data['photos'] = clean_data['photos'].where(clean_data['photos'] > 0, 0)

# Conversion au format datetime
clean_data['date'] = pd.to_datetime(clean_data['date'])

print(clean_data)

