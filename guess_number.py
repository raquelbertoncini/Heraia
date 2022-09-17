import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:#para o loop quando guess for igual ao random do computador
        guess = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, tente novamente. Muito baixo.')
        elif guess > random_number:
            print('Desculpe, tente novamente. Muito alto.')

    print('Parabéns! Você adivinhou o número!')

guess(45)
