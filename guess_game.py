from random import randint


def guess(x):
    answer = randint(1, x)
    while True:
        user_input = int(input(f'Guess number 1~{x}: '))
        if user_input == answer:
            print('you guessed correct ')
            break
        if user_input > answer:
            print('guess again, number is high')
        else:
            print('guess again, number is low')


guess(10)
