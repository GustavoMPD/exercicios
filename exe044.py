
top = 14
vali = 0

for num in range(0, top, 1):
    num += 1
    if (top%num) == 0:
        vali += 1
if vali == 2:
    print('{} é primo'.format(top))
else:
    print('nao e primo')