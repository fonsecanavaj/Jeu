# Julieta Maria Fonseca Nava
# 14/09/23
# Jeu de Devinettes


import random
borne_minimale = 0
borne_maximale = 1000
nombre_a_deviner = random.randint(borne_minimale, borne_maximale)


print(f'J’ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.')
print('À vous de le deviner...')
Essai = input('Entrez votre essai en nombre entier:')

def guess_number():
