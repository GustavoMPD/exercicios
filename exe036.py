valorCasa = float(input('valor da casa '))
valorsalario = float(input('valor do salario  '))
qntAnosPagar = float(input('tempo para pagar em anos '))
valorParcela = valorCasa / (qntAnosPagar * 12)
minimoPagar = valorsalario * 30 / 100

print('o valor das percelas fica em R${}'.format(valorParcela))

if valorParcela <= minimoPagar:
    print('emprestimo permitido')
else:
    print('emprestimo negado')

