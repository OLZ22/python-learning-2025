#Condition exeo
#if
ensoleille = True
if ensoleille:
    print("on va à la plage !")
#if_else
ensoleille = False
if ensoleille:
    print("on va à la plage !")
else:
    print("on reste à la maison !")
#elif
ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")
#and or not
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !") 
#match case
fruit = "orange"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")
#Exo de fin
