#pratiquer les dictionnaire

mon_dictionnaire_fruit = { "pomme":"rouge","banane":"jaune","orange":"orange"}
mon_dictionnaire_fruit["kiwi"] = "vert"
couleur_banane = mon_dictionnaire_fruit["banane"] 
mon_dictionnaire_fruit["pomme"] = "vert"
del mon_dictionnaire_fruit["banane"]
print(mon_dictionnaire_fruit.keys())
