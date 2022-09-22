print('* '*20)
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:#para o loop quando guess for igual ao random do computador
        guess = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('\033[33mDesculpe, tente novamente.\n' 'Muito baixo.\033[m')
            print('- '*15)
        elif guess > random_number:
            print('\033[31mDesculpe, tente novamente.\n' 'Muito alto.\033[m')
            print('- '*15)
    print('\033[30;46mParabéns! Você adivinhou o número!\033[m')
    print('- '*15)

guess(50)
