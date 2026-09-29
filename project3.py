numbers = [0, 0, 0, 0, 0]
biggest = numbers[0]
for i in range(5):
    numbers[i] = int(input("Enter a number: "))
    if numbers[i]> biggest:
        biggest = numbers[i]
print(biggest)