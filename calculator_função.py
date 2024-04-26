def soma(float):
    num1 = float(input("\nInsira o 1º número: "))
    num2 = float(input("\nInsira o 2º número: "))
    print(f"\nA soma dos número é igual a: {num1 + num2}\n" + "\n\n" + ("-"*60))

def subtracao(float):
    num1 = float(input("\nInsira o 1º número: "))
    num2 = float(input("\nInsira o 2º número: "))
    print(f"\nA subtracao dos número é igual a: {num1 - num2}\n" + "\n\n" + ("-"*60))

def multiplicacao(float):
    num1 = float(input("\nInsira o 1º número: "))
    num2 = float(input("\nInsira o 2º número: "))
    print(f"\nA multiplicação dos número é igual a: {num1 * num2}\n" + "\n\n" + ("-"*60))

def divisao(float):
    num1 = float(input("\nInsira o 1º número: "))
    num2 = float(input("\nInsira o 2º número: "))
    print(f"\nA divisão dos número é igual a: {num1 / num2}\n" + "\n\n" + ("-"*60))


print(f"\nProgram that calculate basic mathematic operations!" + "\n\n" + ("-"*60))

contador = 1
while contador == 1:
    op = int(input("\nWich operation do you want to do? \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division \n5 - quit\n\n:  "))
    if op== 1:
        soma(float)
        continue
    elif op== 2:
        subtracao(float)
        continue
    elif op== 3:
        multiplicacao(float)
        continue
    elif op== 4:
        divisao(float)
        continue
    elif op <= 0 or op > 5:
        print ("\nErro ! Insira um valor válido\n" + ("-"*60))
        continue
    else:
     print("\nFim do programa !\n"+ ("-"*60))
     contador += 1
