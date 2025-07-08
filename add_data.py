import pandas as pd
# Boucle pour demander à l'utilisateur s'il veut ajouter un voyage
def demander_ajout_voyage():
    while True:
        reponse = input("Souhaitez-vous ajouter un nouveau voyage ? (Y/N) : ").strip().upper()
        if reponse == 'Y':
            return True
        elif reponse == 'N':
            return False
        else:
            print("Réponse invalide. Tapez Y pour oui ou N pour non.")
# Boucle pour gérer les entrées de l'utilisateur pour les photos
def demander_nb_photos():
    while True:
        try:
            photos = int(input('Combien de photos avez-vous pris ? : '))
            if photos < 0:
                print("Veuillez renseigner une valeur positive")
            else:
                return photos
        except ValueError:
            ("Entrée invalide. Veuillez rentrer un nombre entier")
# Création d'une fonction pour demander la saisie de l'utilisateur
def add_data():
    demander_ajout_voyage()
    city = input('Où êtes-vous allé ? : ')
    date = input('A quelle date ? (AAAA-MM-JJ) : ')
    weather = input('Quel temps faisait-il ? : ')
    mood = input('L\'émotion du voyage (happy, excited, bored...) ? : ')
    photos = demander_nb_photos()
# Création d'un dictionnaire avec les entrées de l'utilisateur
    return {
        'city': city,
        'date': date,
        'weather': weather,
        'mood': mood,
        'photos': photos
    }










