# informe as medidas para saber se foram um triangulo real. Se sim,
# informe qual tipo de triangulo se forma com as medidas

lad1 = int(input('informe o priemria lado '))
lad2 = int(input('informe o segundo lado '))
lad3 = int(input('informe o terseiro lado '))

if lad1 < lad2+lad3 and lad2 < lad1+lad3 and lad3 < lad1+lad2:
    print('são as medidas de um triangulo real')
    if lad1 == lad2 == lad3:
        print('equilatero')
    elif lad1 != lad2 != lad3 != lad1:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('não sao as medidas de um triangulo real')

