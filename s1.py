num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
a = input('select one of them: -, +, *, / :')
if a == '+':
    print(num1 + num2)
if a == '-':
    print(num1 - num2)
if a == '*':
    print(num1 * num2)
if a == '/':
    if num2 == 0 :
        print("Error! you can't divide by zero")
    else :
        print(num1 / num2)
