# faca uma tabuada

#num = int(input('insira um numero para gera a tabuada '))
num = 2
cont = 0
while cont < 10:
    print('{} x {} = {}'.format(num, cont, (num*cont)))
    if cont == 11:
        break
        cont += 1
