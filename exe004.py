# convertta F° -> C°;
# F° -> K°;
# C° -> F°;
# C° -> K°;
# K° -> F°;
# K° -> C°;

tempF = float(input('informe a temperatura em F° para ser convertida em C° '))
tempC = float((tempF-32)/1.8)
print('a temperatura F° para C° é de {}'.format(tempC))

tempF = float(input('informe a temperatura em F° para ser convertida em K° '))
tempK = float