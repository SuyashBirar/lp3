
n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Series:", end=" ")

for i in range(n):
    if i == 0:
        print(a, end=" ")
    elif i == 1:
        print(b, end=" ")
    else:
        c = a + b
        print(c, end=" ")

        a = b
        b = c

        count += 1

print("\nStep Count:", count)
