n = int(input("Enter the number of rows: "))
a = 1
for i in range(n):
    for j in range(i+1):
        print(a, end = " ")
        a += 1
    print()