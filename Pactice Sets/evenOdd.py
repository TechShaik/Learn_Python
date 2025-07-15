# Even numbers from 1 to 50
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print("Even number:", i)
    else:
        print("Odd number:", i)
