from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
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
print(word)