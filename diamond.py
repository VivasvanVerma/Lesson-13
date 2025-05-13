size = int(input("Enter number of rows: "))
if size%2 == 0:
    hd = int(size/2)
else:
    hd = int(size/2)+1
space = hd-1
for i in range(1,hd+1):
    for j in range(1,space+1):
        print(end="")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print()