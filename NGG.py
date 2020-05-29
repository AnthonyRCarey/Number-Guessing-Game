import random


first = 1
last = 10

def game():
    print('------------------------------------')
    print('Welcome to the Number Guessing Game!')
    print('------------------------------------')
    print('')

    randomNum = random.randint(first, last)
    score = 0
    guess = int(input('Pick a number between {} and {}: '.format(first, last)))
    while guess != randomNum:
        try:
            guess = int(input('Pick a number between {} and {}: '.format(first, last)))
            score += 1
            if guess < first or guess > last:
                raise ValueError('Please use a number between {} and {}.'.format(first, last))
        except ValueError as err:
            print('Something went wrong...')
            print(err)
            continue
        if guess > randomNum:
            print('Too high! Try again.')
        elif guess < randomNum:
            print('Too low! Try again.')
        else:
            print('You got it! It took you {} tries.'.format(score))
            print('Closing game, see you next time')
            quit()

game()
