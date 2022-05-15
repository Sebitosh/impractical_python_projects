# Second projet

"""
Objective Use Python to search an English language dictionary for two-word palingrams. Analyze
and optimize the palingram code using the cProfile too
test
"""

import load_dictionary

def pallingrames():
    """Trouve des pallingrames dans un dico"""
    liste_de_mot = load_dictionary.charge('dico.txt')
    mots = set(liste_de_mot)
    liste_palin = []

    for mot in mots:
        end = len(mot)
        reverse = mot[::-1]
        if end > 1:
            for i in range(end):
                if mot[i:] == reverse[:end - i] and reverse[end - i:] in mots:
                    liste_palin.append((mot, reverse[end - i:]))
                if mot[:i] == reverse[end - i:] and reverse[:end - i] in mots:
                    liste_palin.append((reverse[:end - i], mot))

    return liste_palin

pallin = pallingrames()

pallin_sort = sorted(pallin)

print(f"\nNumber of palingrams = {len(pallin_sort)}\n")
for first, second in pallin_sort:
    print(f"{first} {second}")
