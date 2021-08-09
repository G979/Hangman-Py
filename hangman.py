import random

def menu():
    print('Type "play" to play the game, "exit" to quit:')
    first_choice = input()
    if first_choice == "play":
        game()
    elif first_choice == "exit":
        return -1
    else:
        menu()

def game():
    choices = ['python', 'java', 'kotlin', 'javascript']
    pick = random.choice(choices)
    a_string = '-'*len(pick)
    attempts = []
    tries = 0
    while tries < 8 and a_string.find('-') != -1:
        print(f"\n{a_string}")
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        elif not letter.islower() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue
        elif a_string.find(letter) != -1 or letter in attempts:
            print("You've already guessed this letter")
            # tries += 1
        elif pick.find(letter) == -1 and letter not in attempts:
            print("That letter doesn't appear in the word")
            tries += 1
        else:
            cpos = 0
            for character in pick:
                if letter == character:
                    a_string = a_string[:cpos] + a_string[cpos].replace("-", letter) + a_string[cpos + 1:]
                cpos += 1
        attempts.append(letter)
    if tries == 8:
        print("You lost!")
        print()
    else:
        print("")
        print(pick)
        print("You guessed the word!")
        print("You survived!")
        print()


print("H A N G M A N")
menu()
