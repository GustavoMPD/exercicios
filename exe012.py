# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com
# 5% de desconto

precReal = float(input('informe o valo de produto para aplica o desconto'))
novPrec = precReal - (precReal*5/100)
print('o valor atual com desconto é = {}'.format(novPrec))