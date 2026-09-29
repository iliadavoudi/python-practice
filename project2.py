numbers = [11, 34, 62, 73, 9]
for i in range(len(numbers)):
    num = int(input("Enter a number: "))
    if num == numbers[i]:
        print("True")
        print("index" , i)
        print(numbers)
    else:
        print("False")
        numbers.append(num)
        print(numbers)
    ask = input("Would you like to continue? ")
    if ask == "no":
        print("Goodbye!")
        break