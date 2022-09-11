from random import randint


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = randint(low, high)
        else:
            guess = high  # could also be low b/c high = low
        feedback = input(
            f'Is {guess} is high (H), or low (L), or correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay, Computer guessed the correct number {guess}')


computer_guess(10)
