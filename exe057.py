

s = str(input("imforme o seu sexo "))

while s not in 'mf':
        s = input("valor invalido: gidite o seu sexo ")
if s == 'f':
        print('seu sexo é feminino')
else:
        print('seu sexo é masculino')