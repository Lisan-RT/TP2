def affiche():
    resultat = ""
    for i in range(1, 16):  # 1 à 15 inclus
        if i % 15 == 0:
            resultat += "FrisBee"
        elif i % 3 == 0:
            resultat += "Fizz"
        elif i % 5 == 0:
            resultat += "Buzz"
        else:
            resultat += str(i)
    return resultat

