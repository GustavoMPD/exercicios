# calcule a hipotenisa de um triangulo retangulo

import math

catOposto = float(input('informe o cateto oposto '))
catAdjacente  = float(input('informe o cateto adjacente '))

hipotenusa = math.hypot(catOposto, catAdjacente)

print('a hipotenusa é {:.2f}'.format(hipotenusa))
