from random_words import RandomWords
# print(word)

print('\nWelcome to @TheLukeRussell\'s Hangman Game! ')
print('\n\tThe instructions are simple, guess the random word before time runs out for the Hangman')

msg = '\nDo you think that you can save him?'
shall = input("%s (Y/N) " % msg).lower() == 'y'
def yn_choice(message, default='y'):
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice = input("%s (%s) " % (message, choices))
    values = ('y', 'yes', '') if choices == 'Y/n' else ('y', 'yes')
    return choice.strip().lower() in values

print('\nFirst things first, what is your name?')
name = input( )

print('\nOk ' + name + '! let\'s get started!')

number_of_guesses = 0
# number_of_guesses = number_of_guesses + 1

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
            print( "    |")
            print("|    O")
            print("|")
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
    elif (number_of_guesses == 8):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|   \|/")
        print( "|    |")
        print( "|  _/ \ ")
        print( "|________")
    elif (number_of_guesses == 8):
        print( "_________")
        print( "|    |")
        print( "|    O")
        print( "|   \|/")
        print( "|    |")
        print( "|  _/ \_ ")
        print( "|________")
        
rw = RandomWords()
word = rw.random_word()

def hangMan():
    number_of_guesses = 0
    word = rw.random_word()
    word_list = list(word)
    word_blanks = '__'*len(word)
    blanks_list = list(word_blanks)
    new_blanks_list = list(word_blanks)
    guess_list = []

    print(show_hang(number_of_guesses, word))
    print('/n ' + ''.join(blanks_list))
    print('\nGuess a letter!')

    while number_of_guesses < 8:
        guess = input("> ")
        guess = guess.lower()
    
        if len(guess) > 1:
            print('Yo chill, only one letter at a time')
        elif guess == '':
            print('You can choose a letter ya know?')
        elif guess in guess_list:
            print('You already guessed that letter')
            print(' ').join(guess_list)
        else:
            # guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i+1
        
            if new_blanks_list == blanks_list:
                print('Your letter isn\'t here')
                number_of_guesses = number_of_guesses + 1
                print(show_hang(number_of_guesses, word))

                if number_of_guesses < 8:
                    print('Keep guessing')
                    print('').join(blanks_list)
        
            elif word_list != blanks_list:
                blank_list = new_blanks_list[:]
                print('').join(blanks_list)

                if word_list == blanks_list:
                    print('\n You Win!!')
                else:
                    print: 'guess another'
                    
hangMan()