def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat


    if n%3==0 and n%5==0:
        return "fizzbuzz"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return f"{n} nest pas un multiple de 3 et/ou de 5"

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))


