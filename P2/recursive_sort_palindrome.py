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


def is_palindrome(string) -> bool:
    """recursivly identify palindrome"""
    if len(string) == 0 or len(string) == 1:
        return True
    if not string[0] == string[len(string)-1]:
        return False
    return is_palindrome(string[1:len(string)-1])


def recursive_palin():
    """recursive version of finding palindrome"""

    liste_de_mot = load_dictionary.charge('dico.txt')
    liste_palin = []

    for mot in liste_de_mot:
        if is_palindrome(mot):
            liste_palin.append(mot)

    return liste_palin


liste = recursive_palin()

print(f"\nNumber of palindromes found = {len(liste)}\n")
print(*liste, sep='\n')
