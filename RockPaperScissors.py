import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please'))

    if choice == 1:
        choice_name = 'Rock\n'
    elif choice == 2:
        choice_name = 'Paper\n'
    else:
        choice_name = 'Scissors\n'

    print('Your choice is: \n', choice_name)
    print('Computers turn...\n')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock\n'
    elif choice == 2:
        comp_choice_name = 'Paper\n'
    else:
        comp_choice_name = 'Scissors\n'

    print("Computers choice is: \n", comp_choice_name)
    print(choice_name, 'VS \n', comp_choice_name)

    if choice == comp_choice:
        print('Its a draw\n', end="")
        result = "DRAW"

    if (choice == 1 and comp_choice == 2):
        print('Paper wins\n', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('Paper wins\n', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins \n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins \n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins\n', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins\n', end="")
        result = 'Scissors'

    if result == 'DRAW':
            print("Its a tie\n")
    if result == choice_name:
            print("User wins\n")
    else:
        print("Computer wins\n")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break
    
print("Thanks for playing!")