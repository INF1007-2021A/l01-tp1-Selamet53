def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    position_voiture2 = distance
    position_voiture1=position_voiture2-distance

    while position_voiture1!=position_voiture2:
        position_voiture1+=v1
        position_voiture2-=v2

    position_voiture1=position_voiture1

    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = position_voiture1=position_voiture2

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
