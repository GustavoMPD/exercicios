# sorteie um ente quatro nomes

import random

nome1 = str(input('escreva o nome '))
nome2 = str(input('escreva o nome '))
nome3 = str(input('escreva o nome '))
nome4 = str(input('escreva o nome '))
lis = ['aaa', 'bbb', 'ccc', 'ddd']
sorteio = random.choice(lis)

print('o nome escolhido é {}'.format(sorteio))
