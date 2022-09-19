print('* '*20)

import random

def jogar():
    user = input('Pedra(P), papel(A) ou tesoura(T)? '). upper()
    computer = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

    if (user == 'T' and computer == 'TESOURA') or (user == 'A' and computer == 'PAPEL') or (user == 'P' and computer == 'PEDRA'):
        print(f'{computer}')
        return 'Empate'

    if ganha(user, computer):
        print(f'{computer}')
        return 'Você venceu!'

    else:
        print(f'{computer}')
        return 'Você perdeu'
 

def ganha(jogador, computador):
    if (jogador == 'P' and computador == 'TESOURA') or (jogador == 'T' and computador == 'PAPEL') or (jogador == 'A' and computador == 'PEDRA'):
        return True
# pedra > tesoura, tesoura > papel, papel > pedra
# essas são as condições de GANHA, então função retorna TRUE


vezes = int(input('Quantas rodadas você quer jogar? '))
rodada = 0

while rodada < vezes:
    rodada += 1

    print(jogar())



