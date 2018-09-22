# Exercício 1
# Cálculos da velocidade e multa por excesso de velocidade

velocidade = float(input("Entre com o valor da velocidade:"))

if velocidade > 80: 
    print("Você foi multado por excesso de velocidade!")
    multa = ((velocidade - 80) * 5)
    print('Valor da Multa: R$',multa)
else:
    print("Você está dentro do limite de velocidade permitida!")
