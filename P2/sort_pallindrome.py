# Second project

"""
In this chapter, you’ll load dictionary files from the internet and use
Python to discover first palindromes and then the more complex palin-
grams in those files. Then you’ll use a tool called cProfile to analyze your
palingram code so that you can make it more performant. Finally, you’ll sift
through the palingrams to see how many have an “aggressive” nature

Objective: Use Python to search an English language dictionary file for palindromes.
"""

import load_dictionary

liste_de_mot = load_dictionary.charge('dico.txt')
liste_palin = []

for mot in liste_de_mot:
    if len(mot) > 1 and mot == mot[::-1]:
        liste_palin.append(mot)

print(f"\nNumber of palindromes found = {len(liste_palin)}\n")
print(*liste_palin, sep='\n')
