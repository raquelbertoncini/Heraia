print('* '*20)



score_user = 0
score_comp = 0

import random

def jogar():
    print('* '*15)
    user = input('Pedra(P), papel(A) ou tesoura(T)? '). upper()
    computer = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
   

    global score_user
    global score_comp

    if (user == 'T' and computer == 'TESOURA') or (user == 'A' and computer == 'PAPEL') or (user == 'P' and computer == 'PEDRA'):
        print(f'Computador: {computer}')
        return 'Empate'

    if ganha(user, computer):
        print(f'Computador: {computer}')
        score_user += 1
        return 'Você venceu!'
     
    else:
        print(f'Computador: {computer}')
        score_comp += 1
        return 'Você perdeu'
      

def ganha(jogador, computador):
    if (jogador == 'P' and computador == 'TESOURA') or (jogador == 'T' and computador == 'PAPEL') or (jogador == 'A' and computador == 'PEDRA'):
        return True
    # pedra > tesoura, tesoura > papel, papel > pedra
    # essas são as condições de GANHA, então função retorna TRUE

try:
    vezes = int(input('Quantas rodadas você quer jogar? '))
    rodada = 0
    while rodada < vezes:
            rodada += 1

            print(jogar())

except ValueError:

    print('\033[30;41mVocê não digitou o número de rodadas!\033[m')
    


print('* '*15)

if score_comp > score_user:
    print('\033[34mO COMPUTADOR FOI O VENCEDOR!\033[m')

elif score_comp < score_user:
    print('\033[34mVOCÊ FOI A CAMPEÃ!\033[m')

else:
    print('\033[34mDessa vez não deu pra ninguém.\033[m')

print(f'\033[33mComputador {score_comp}\n'
f'Você       {score_user}\033[m')
print('* '*15)


