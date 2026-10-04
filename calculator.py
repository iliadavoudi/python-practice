while True :

    num1 =input('Enter a number: ')
    num2 =input('Enter another number: ')
    if num1 == "" or num2 == "" :
        print("Error! you must enter a number")
        continue
    num1 = int(num1)
    num2 = int(num2)

    op = input('select one of them: -, +, *, / :')
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Error! you must enter a math operator")
        continue
    if op == '+':
        print(num1 + num2)
    if op == '-':
        print(num1 - num2)
    if op == '*':
        print(num1 * num2)
    if op == '/':
        if num2 == 0 :
            print("Error! you can't divide by zero")
        else :
            print(num1 / num2)
    ask = input("do you want continue? ")
    if ask == "No" :
        print("goodbye")
        break
