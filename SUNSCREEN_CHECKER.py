badIngredients = ["Octinoxate", "Oxybenzone", "Benzophenone-3", "Avobenzone", "benzophenone",
                  "Cylcopentasiloxane", "Cyclomethicone", "Formaldehyde", "Diazolidinyl", "urea",
                  "DMDM", "Hydantoin", "Hydroxymethylglycinate", "Methylisothiazolinone", "Octyl",
                  "methoxycinnamate", "Parabens", "Sodium", "lauryl", "laureth", "sulfate", "SLS", "SLES",
                  "Butylparaben", "4-methylbenzylidene", "camphor", "Octocrylene", "Para-aminobenzoic", "acid",
                  "PABA", "Methylparaben", "Ethylparaben", "Propylparaben", "Butylparaben", "Benzylparaben",
                  "Triclosan"]

numBad = 0


ingredients = input ("Enter ingredients: ")
ingredients = ingredients.replace(",", " ")
ingredientList = ingredients.split(" ")


for i in (range (len (ingredientList))):
    for j in (range (len (badIngredients))):
        if ingredientList[i].lower() == badIngredients[j].lower():
            numBad += 1
            print (badIngredients[j])

print (numBad)
