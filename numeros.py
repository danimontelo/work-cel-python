num1 = int(input("Digite o valor do primeiro número:"))
num2 = int(input("Digite o valor do segundo número:"))
num3 = int(input("Digite o valor do terceiro número:"))

if num1 > num2 and num1 > num3:
    print('O primeiro número é o maior:', num1)
elif num2 > num1 and num2 > num3:
    print('O segundo número é o maior:', num2)
else:
    print('O terceiro número é o maior:', num3)

if num1 < num2 and num1 < num3:
    print('O primeiro número é o menor:', num1)
elif num2 < num1 and num2 < num3:
    print('O segundo número é o menor:', num2)
else:
    print('O terceiro número é o menor:', num3)