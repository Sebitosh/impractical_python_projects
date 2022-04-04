"""
Charge un document texte comme une liste

:argument
-Nom du fichier texte

:exception
-IOError si le nom ne trouve pas de fichier

:returns
-liste de tout les mots du fichier texte en lowercase

Requires-import sys
"""

import sys


def charge(file):
    """Ouvre le fichier texte et retourne la liste contenant les Strings"""
    try:
        with open(file) as in_file:
            charge_txt = in_file.read().strip().split('\n')
            charge_txt = [x.lower() for x in charge_txt]
            return charge_txt
    except IOError as e:
        print(f"{e}\nErreur ouverture {file}. Termination du programme",
              file=sys.stderr)
        sys.exit(1)
