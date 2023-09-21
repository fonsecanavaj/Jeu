# Julieta María Fonseca Nava
# 21/09/23
# TP2 - Jeu de devinettes

import random

score = 0


def exit_game():
    print("\nMerci et au revoir...")
    exit()
    

borne_maximale = int(input("Choisissez la borne maximale: "))
borne_minimale = int(input("Choisissez la borne minimale: "))
nombre_a_deviner = random.randint(borne_minimale, borne_maximale)
message = f"J’ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}. À vous de le deviner..."
print(message)
essai = int(input("\nEntrez votre essai: "))


while True:

    if essai > nombre_a_deviner:
        print(f"\nMauvais choix, le nombre est plus petit que {essai}")
        score +=1
        essai = int(input("Entrez votre essai: "))

    elif essai < nombre_a_deviner:
        print(f"\nMauvaise réponse, le nombre est plus grand que {essai}")
        score +=1
        essai = int(input("Entrez votre essai: "))

    else:
        score +=1
        print("\nBravo! Bonne réponse")
        print(f"Vous avez réussi en: {score} essai(s)")
        confirmation = input("\nVoulez-vous faire une autre partie (o/n)? ")

        if confirmation == "o":
            borne_maximale = int(input("\nChoisissez la borne maximale: "))
            borne_minimale = int(input("Choisissez la borne minimale: "))
            nombre_a_deviner = random.randint(borne_minimale, borne_maximale)
            essai = int(input("Entrez votre essai: "))
            score = 0

        else:
            exit_game()
