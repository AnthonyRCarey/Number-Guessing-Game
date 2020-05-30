import random


def startGame():
    # Welcome the user
    print('\nWelcome to the Number Guessing Game!\n')

    # Variables
    gameBegin = True
    highScore = ''
    score = 0
    answer = random.randint(1, 10)

    # Game begins
    while(gameBegin):
        try:
            guess = int(input('Input your guess between 1 and 10: '))
            if guess > 10 or guess < 1:
                score += 1
                print('\nYour guess needs to be between 1 and 10.\n')
            elif guess > answer:
                score += 1
                print('\nToo high! Try again.\n')
            elif guess < answer:
                score += 1
                print('\nToo low! Try again.\n')
            elif guess == answer:
                score += 1
                gameBegin = False
                if highScore == '' or highScore > score:
                    highScore = score
                print('\nYou got it! It took you {} tries.\n'.format(score))
                # Exceeds
                while(True):
                    startAgain = input('Want to play again? [Y/N]: ')
                    if startAgain[0].lower() == 'y':
                        gameBegin = True
                        score = 0
                        answer = random.randint(1, 10)
                        print('\nThe current high score is: {}\n'.format(highScore))
                        break
                    else:
                        print('\nThanks for playing!\nClosing game...')
                        quit()
        except ValueError:
            print('Something went wrong...')
    # Game ends

startGame()
