import random

restart = 'Y'
words = ('thunderbolt', 'pickles', 'imagination', 'catastrophe', 'backpack',
         'strawberry', 'philosophy', 'terminal', 'restriction', 'wardrobe',
         'tortilla', 'tornado')

while True:
    watchword = random.choice(words).upper()
    lives = 7
    used_letters = []
    current_word = len(watchword) * '_ '

    while restart == 'Y':
        print(f'You have {lives} lives left and you have used these letters: {used_letters}')
        print(f'Current word: {current_word}')
        letter = input('Guess a letter: ').upper()
        used_letters.append(letter)

        if letter in watchword:
            for index, character in enumerate(watchword):
                if character == letter:
                    current_word.replace(current_word[index], letter) #tu mi nie dziala, uzyc gita zeby miec wersje sprzed kombinowaniem

        # current_word.replace(current_word.index(letter), letter)
        else:
            print(f'Your letter \'{letter}\' is not in the word')
            lives -= 1

        # restart = input('Type \'Y\' if you want to play again.')
