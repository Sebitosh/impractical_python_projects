# First project of the book

"""
In this warm-up project, you’ll write a simple Python program that gen-
erates nutty names by randomly combining first names and surnames.
With any luck, you’ll produce a plethora of aliases that would make any
sidekick proud. You’ll also review best-practice coding guidelines and
apply external programs that will help you write code that conforms to
those guidelines.
Psych not your thing? Replace the names in my list in the code with
your own jokes or theme. You could just as easily turn this project into a
Game of Thrones name generator...


objective : Randomly generate funny sidekick names
using Python code that conforms to established style guidelines

personal objective : adapt this to make a random
revolutionary communist nickname generator
"""

import random
from termcolor import colored


def main():
    """Choisis deux noms aléatoires dans les tuples et les affiche"""

    print("Bienvenue au générateur de nom pour révolutionnaires \n")
    print("Assigné par la mémoire du grand Lénine, votre nom est : \n\n")

    first = ('Vladimir', 'Joseph', 'Julien', "Rosa",
             "Karl", 'Friederich', 'Nikolaï', "Fidel",
             'Raoul', 'Marco', 'Marc', 'Fabien', 'George',
             'Pablo', 'Ernesto', 'Alice', 'Jean-Luc', 'Adrien',
             'Gaby', 'Anouk', 'Robin', 'Phillipe', 'Benoît',
             'Alexandra', 'Evgeny', 'Leon', 'nikita', 'Antonio', 'Leonid',
             'Hugo', 'Ludo', 'Thomas', "Patrice", 'Nelson',
             'Angela', 'Slavoj', 'Cédric', 'Cloé',
             'Raùl', 'Robert', 'Peter', 'Maria', 'Nabil',
             'Nadia', 'Sofie', 'David', 'Antoine',
             'Jos', 'Kim', 'Françoise', 'Elisa', 'Petya',
             "Caroline", 'Germain', 'Amandine', 'Jeronimo', 'Carlos')

    middle = ("'Présent chaque saison'", "'Che'", "'Le soleil dans la poche'")

    last = ('Hedebouw', 'Pestieau', 'Lenine', 'Trotsky',
            'Lahaut', 'Melenchon', 'Jacquemotte', 'Mertens',
            'Boukharine', 'Kautsky', 'Marx', 'Engels', 'De Witt',
            'De Smet', 'Sankara', 'Lumumba', 'Brejnev', 'Andropov',
            'Chavez', 'Moscufo', 'Vindevoghel', 'Branco', 'Morozov',
            'Zijeck', 'Kolmogorov', "Castro", 'Guevara', 'Kollontaï',
            'Van Hees',
            'Ruffin', 'Marchais', 'Hue', 'Gropi', 'Merckx',
            'Schepman', 'Piketty', 'Obolensky', 'Allende')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        if random.randint(0, 1) == 0:
            middle_name = random.choice(middle)
            print(colored(f"{first_name} {middle_name} {last_name}", 'red', None, ['bold']))
            print("\n\n")
        else:
            print(colored(f"{first_name} {last_name}", 'red', None, ['bold']))
            print("\n\n")

        try_again = input(
            "Encore ? (Appuyez sur n pour quitter ou autre pour continuer)"
            "\n ")
        if try_again.lower() == 'n':
            break

    input("\nAppuyez sur enter pour quitter.")


if __name__ == '__main__':
    main()
