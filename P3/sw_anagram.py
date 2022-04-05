# third Project

"""
Objective: Use Python and a dictionary file to find all the single-word anagrams for a given English
word or single name. You can read instructions for finding and loading dictionary files at
the start of Chapter 2.
"""

from P2 import load_dictionary

liste = load_dictionary.charge('dico.txt')
user_input = input('Entrez un mot pour trouver ses anagrames').lower()
anagram_list = []

sorted_user_input = sorted(user_input)

for mot in liste:
    sort_mot = sorted(mot.lower())
    if mot != user_input:
        if sort_mot == sorted_user_input:
            anagram_list.append(mot)


if len(anagram_list) == 0:
    print("Aucuns anagrames trouvés, choisissez un nouveau mots ou dictionnaire")
else:
    print(f"{len(anagram_list)} anagrames trouvés\n")
    print(*anagram_list, sep='\n')
