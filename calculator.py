#print(f"\nProgram that calculate basic mathematic operations!")
#num1 = float(input("\nEnter the 1º number: "))
#num2 = float(input("\nEnter the 2º number: "))
#op = int(input("\nWich operation do you want to do? \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division \n5 - quit\n: "))
#if op== 1:
#   print(f"\nThe calculation is {num1} + 2{num2}= {num1+num2:.2f}\n")
#elif op== 2:
#    print(f"\nThe calculation is {num1} - {num2}= {num1 - num2:.2f}\n")
#elif op== 3:
#    print(f"\nThe calculation is {num1} x {num2}= {num1 * num2:.2f}\n")
#elif op== 4:
#    print(f"\nThe calculation is {num1} / {num2}= {num1 / num2:.2f}\n")
#else:
#    quit()

#New program with while else
print(f"\nProgram that calculate basic mathematic operations!")
op = 0
while op < 5:
    op = int(input("\nWich operation do you want to do? \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division \n5 - quit\n\n:  "))
    if op== 1:
        num1 = float(input("\nEnter the 1º number: "))
        num2 = float(input("\nEnter the 2º number: "))
        print(f"\nThe calculation is {num1} + 2{num2} = {num1+num2:.2f}\n" + ("-"*60))
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
else:
    print("\nFim do programa !\n"+ ("-"*60))
    quit
