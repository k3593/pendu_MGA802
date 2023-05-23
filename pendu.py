# -*- coding: utf-8 -*-
"""
Code qui permet de jouer au pendu
"""

import random
import string


def initialisation():
    # initialisation du nombre de vies
    nb_vies = 6
    # initialisation de la chaine de caractère qui contiendra les lettres deja demandees
    letter_asked = ""
    return nb_vies, letter_asked


def selection_mot():
    return random.choice(open("mots_pendu.txt", "r").read().split('\n'))


def affichage(mot, vie, lettres = ""):
    # creation de la chaine de caractère à afficher
    aff = ''
    for i in mot:
        if i in lettres:
            aff += i + ' '
        else:
            aff += '_ '
    
    # cas où le mot est trouvé
    if '_' not in aff: 
        print(f'BRAVO ! Tu as réussi a trouver le mot : {mot}.')

    # cas où le joueur n'a plus de vie
    elif vie == 0:
        print(f"Zut, tu n'as plus de vie. Perdu ! Le mot était {mot}")

    # cas où la partie continue
    else:
        print(aff, f", il te reste {vie} vies pour trouver le mot\n")
        # rapeler au joueur les lettres déjà demandées
        if len(lettres) != 0:
            print(f"Tu as déjà testé les lettres suivantes : {lettres}")

    return aff


def jeu(vies, asked, mot):
    # premier affichage
    guess = affichage(mot, vies)

    # début du jeu et continuation tant que la partie n'est pas perdue ou gagnée
    while vies > 0 and '_' in guess:
        # Récupération de la lettre
        lettre = str(input('lettre : '))

        # cas où le caractère rentré par l'utilisateur est bien dans l'alphabet ascii
        if lettre in string.ascii_letters:
            lettre = lettre.lower()  # mettre en minuscule pour unifier

            # cas où l'utilisateur avait déjà demandé cette lettre
            if lettre in asked:
                print('lettre deja testee ! \n')

            else:
                # si la lettre n'est pas dans le mot, perdre une vie
                if lettre not in mot:
                    print('Non.')
                    vies -= 1
                # rajout de la nouvelle lettre à la chaine de caractère
                asked += lettre
                # affichage en prennant en compte la nouvelle lettre
                guess = affichage(mot, vies, asked)

        # cas où le caractère rentré par l'utilisateur n'est pas dans l'alphabet ascii
        else:
            print("Ce n'est pas une lettre")


if __name__ == '__main__':
    # initialisation des variable
    vies_restante, asked = initialisation()

    # selection aléatoire d'un mot dans la liste
    mot = selection_mot()

    # lancement du jeu
    jeu(vies_restante, asked, mot)

