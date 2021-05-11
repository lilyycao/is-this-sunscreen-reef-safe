# This program is a binary search algorithm to check sunscreen ingredients
# Last edited by Fiona Hila: May 10, 2021

badIngredients = ["Octinoxate", "Oxybenzone", "Benzophenone-3", "Avobenzone", "benzophenone",
                  "Cylcopentasiloxane", "Cyclomethicone", "Formaldehyde", "Diazolidinyl", "urea",
                  "DMDM", "Hydantoin", "Hydroxymethylglycinate", "Methylisothiazolinone", "Octyl",
                  "methoxycinnamate", "Parabens", "Sodium", "lauryl", "laureth", "sulfate", "SLS", "SLES",
                  "Butylparaben", "4-methylbenzylidene", "camphor", "Octocrylene", "Para-aminobenzoic", "acid",
                  "PABA", "Methylparaben", "Ethylparaben", "Propylparaben", "Butylparaben", "Benzylparaben",
                  "Triclosan"]

badIngredients.sort()

numBad = 0

# input sunscreen ingredient list and turn into a list with each word
ingredients = input ("Enter ingredients: ")
ingredients = ingredients.replace(",", " ")
ingredientList = ingredients.split(" ")        

# perform binary search
for i in (range (len (ingredientList))):
    current = ingredientList[i].lower()
    low = 0
    high = len (badIngredients) - 1
    
    while (low <= high):

        mid = (low + high) // 2

        if (current == badIngredients[mid].lower()):
            numBad += 1
            print (ingredientList[i])
            break
        elif (current < badIngredients[mid].lower()):
            high = mid - 1
        else:
            low = mid + 1
        
print (numBad)
