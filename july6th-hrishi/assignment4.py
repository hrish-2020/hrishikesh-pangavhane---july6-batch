print("welcome to hrishi calculator")
while True:
    print("enter + for addition")
    print('enter - for substraction')
    print('enter * for multiplication')
    print('enter / for division')
    print('enter % for modulos')
    choice = input()

    if choice == "+":
        n1 = int(input("please enter first no"))
        n2 = int(input("please enter second no"))
        print("the additon is ",n1+n2)
    elif choice == "-":
        n1 = int(input("please enter first no"))
        n2 = int(input("please enter second no"))
        print("the substraction is",n1-n2)
    elif choice == "*":
        n1 = int(input("please enter first no"))
        n2 = int(input("please enter second no"))
        print("the multiplication is",n1*n2)
    elif choice == "/":
        n1 = int(input("please enter first no"))
        n2 = int(input("please enter second no"))
        print("the division is",n1/n2)
    elif choice == "%":
        n1 = int(input("please enter first no"))
        n2 = int(input("please enter second no"))
        print("the modulus is",n1%n2)
    elif choice == "exit":
        break

else:
    print("enter valid symbol")