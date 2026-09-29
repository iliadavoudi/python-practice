numbers1 = [0, 0, 0, 0, 0]

for i in range(5):
    numbers1[i] = int(input("Enter a number: "))

smallest = numbers1[0]
biggest = numbers1[0]

for i in range(5):
    if numbers1[i] > biggest:
        biggest = numbers1[i]

    if numbers1[i] < smallest:
        smallest = numbers1[i]

for i in range(5):
    if numbers1[i] == biggest:
        print("Biggest number index:", i)

print("Biggest:", biggest)
print("Smallest:", smallest)