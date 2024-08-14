#
# Shawntel Hamilton
# 6/4/24
# Program dice game that ask users roll amount between 5 and 15 and display game results to user
#

import random


def main():
    # Get initial roll input
    roll = int(input('How many times do you want to roll the die? '))

    # Checks to see if user input correct range of roll number
    while roll <= 4 or roll >= 14:
        print('Enter a number between 5 and 15.')
        roll = int(input('How many times do you want to roll the die? '))
    else:
        roll_die(roll)


def roll_die(roll):

    # for loop to roll die specific number of time
    for count in range(1, roll + 1):

        # Generates random number
        number = random.randint(1, 20)

        # Checks if modulus of number variable equal to 0 - 3 and 20 and output correct die output with roll number
        if number % 4 == 0:
            print(f'Roll {count}: {number} ==> Sword')
        elif number % 4 == 1:
            print(f'Roll {count}: {number} ==> Shield')
        elif number % 4 == 2:
            print(f'Roll {count}: {number} ==> Spell')
        elif number % 4 == 3:
            print(f'Roll {count}: {number} ==> Potion')
        elif number == 20:
            print(f'Roll {count}: {number} ==> CRITICAL HIT')
    print('Thanks for playing!')


main()
