class bcolors:
    Purple = '\033[95m'
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from random_words import RandomWords
# print(word)

print(f'{bcolors.Purple}{bcolors.BOLD}\n\t\tWelcome to @TheLukeRussell\'s Hangman Game!{bcolors.ENDC}')
print(f'{bcolors.Yellow}\n\tThe instructions are simple, guess the random word before time runs out for the Hangman{bcolors.ENDC}')

msg = f'{bcolors.Red}\nDo you think that you can save him? '
shall = input("%s (Y/N) " % msg).lower() == 'y'
def yn_choice(message, default='y'):
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice = input("%s (%s) " % (message, choices))
    values = ('y', 'yes', '') if choices == 'Y/n' else ('y', 'yes')
    return choice.strip().lower() in values

print(f'{bcolors.Blue}\nFirst things first, what is your name?')
name = input( )

print(f'\nOk ' + name + '! let\'s get started!')

number_of_guesses = 0
number_of_guesses = number_of_guesses + 1

def show_hang(number_of_guesses, word):
    if (number_of_guesses == 0):
        print( "_________")
        print( "|    |")
        print( "|")
        print( "|")
        print( "|")
        print( "|")
        print( "|________")
    elif (number_of_guesses == 1):
        print( "________")
        print( "     |")
        print( "|    O")
        print( "|")
        print( "|")
        print( "|")
        print( "|________")   
    elif (number_of_guesses == 2):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|    |")
        print( "|")
        print( "|")
        print( "|________")   
    elif (number_of_guesses == 3):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|    |")
        print( "|    |")
        print( "|")
        print( "|________")   
    elif (number_of_guesses == 4):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|    |/")
        print( "|    | ")
        print( "|")
        print( "|________")   
    elif (number_of_guesses == 5):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|   \|/")
        print( "|    | ")
        print( "|")
        print( "|________")   
    elif (number_of_guesses == 6):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|   \|/")
        print( "|    |")
        print( "|     \ ")
        print( "|________")   
    elif (number_of_guesses == 7):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|   \|/")
        print( "|    |")
        print( "|   / \ ")
        print( "|________")

rw = RandomWords()
word = rw.random_word()

def hangMan():
    number_of_guesses = 0
    word = rw.random_word()
    word_list = list(word)
    word_blanks = '_'*len(word) # "__________"
    # ['_', '_', '_']
    blanks_list = list(word_blanks) # 
    # ['_', 'u', '_']
    new_blanks_list = list(word_blanks)
    guess_list = []

    print(f'\n{bcolors.Green}')

    show_hang(number_of_guesses, word)

    print('\n')
    print("" + ' '.join(blanks_list))
    print('\nGuess a letter!')
    # print(word)

    while number_of_guesses < 7:
        guess = input("> ")
        guess = guess.lower()
    
        if len(guess) > 1:
            print('Yo chill, only one letter at a time')
        elif guess == '':
            print('You can choose a letter ya know?')
        elif guess in guess_list:
            print('You already guessed that letter')
            print('These are the letters you have guessed ' + ', '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if (guess not in word_list):
                print('Your letter isn\'t here')
                number_of_guesses = number_of_guesses + 1
                show_hang(number_of_guesses, word)

                if number_of_guesses < 7:
                    print('Keep guessing')
                    print(''.join(blanks_list))

                else:
                    print(f'\n{bcolors.Red}{bcolors.BOLD}Oh no, you killed him!{bcolors.ENDC}')
                    break

            else:

                blank_list = new_blanks_list
                print(''.join(blanks_list))
                show_hang(number_of_guesses, word)

                if word_list == new_blanks_list:
                    print("" + ' '.join(new_blanks_list))
                    print(f'{bcolors.BOLD}\nYou Win!!{bcolors.ENDC}')
                    break
                else:
                    print('Great guess, keep Guessing!')
                    print("" + ' '.join(new_blanks_list))
                    # break
                    
hangMan()