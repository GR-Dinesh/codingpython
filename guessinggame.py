import random

n = random.randint(1,10)
#print(f'{n}')
rounds = 5

for _ in range(rounds):
    guess = int(input('Enter the number to guess from 1 - 10:'))
    if guess > n:
        print('You guessed it higher')
    elif guess < n:
        print('You guessed it lower')
    else:
        print(f'You guessed it right:{n}')
        exit()
