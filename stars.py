s = input("Enter symbol: ")
n = int(input("Enter the number of symbols: "))
for i in range(n):
    for j in range(i+1):
        print(s , end = "")
    print()