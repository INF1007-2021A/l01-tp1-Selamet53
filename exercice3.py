
def decomposer(secondes):


    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes/(60*60*24*365)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = (annees-round(annees))*(52+1/7)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = (semaines-round(semaines))*7

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = (jours-round(jours))*24

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = (heures-round(heures))*60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = (minutes-round(minutes))*60

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(round(annees) ,round(semaines) ,round(jours) ,round(heures) ,round(minutes) ,round(secondes))

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
