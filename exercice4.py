import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    vitesseInitiale_m=vitesseInitiale*(1000/3600)
    vitesseFinale_m=vitesseFinale*(1000/3600)
    accélération_m=(vitesseFinale_m-vitesseInitiale_m)/duree
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale =(vitesseInitiale_m*duree)+(1/2)*accélération_m*(duree**2)+positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
