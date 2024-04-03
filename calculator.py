print(f"\nProgram that calculate basic mathematic operations!")
contador = 1
while contador == 1:
    op = int(input("\nWich operation do you want to do? \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division \n5 - quit\n\n:  "))
    if op== 1:
        num1 = float(input("\nEnter the 1º number: "))
        num2 = float(input("\nEnter the 2º number: "))
        print(f"\nThe calculation is {num1} + {num2} = {num1+num2:.2f}\n" + ("-"*60))
    elif op== 2:
        num1 = float(input("\nEnter the 1º number: "))
        num2 = float(input("\nEnter the 2º number: "))
        print(f"\nThe calculation is {num1} - {num2} = {num1 - num2:.2f}\n" + ("-"*60))
    elif op== 3:
        num1 = float(input("\nEnter the 1º number: "))
        num2 = float(input("\nEnter the 2º number: "))
        print(f"\nThe calculation is {num1} x {num2} = {num1 * num2:.2f}\n" + ("-"*60))
    elif op== 4:
        num1 = float(input("\nEnter the 1º number: "))
        num2 = float(input("\nEnter the 2º number: "))
        print(f"\nThe calculation is {num1} / {num2} = {num1 / num2:.2f}\n" + ("-"*60))
    elif op <= 0 or op > 5:
        print ("\nErro ! Insira um valor válido\n" + ("-"*60))
    else:
     print("\nFim do programa !\n"+ ("-"*60))
     contador += 1
     
