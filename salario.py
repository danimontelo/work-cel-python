salario = float(input('Digite o valor do seu salário:'))

if salario > 1.250:
    reajuste = salario + (salario * 0.10)
    print('Seu salário foi reajustado para: R$', reajuste)
else:
    reajuste = salario + (salario * 0.15)
    print('Seu salário foi reajustado para: R$', reajuste)