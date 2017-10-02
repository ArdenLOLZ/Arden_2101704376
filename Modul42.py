numbers= []
count = 0
check = []
for i in range (0,10):
    temp = input()
    numbers.append(int(temp))
for i in range (0,10):
    if numbers[i]%42!=0:
        num = numbers[i]%42
        check.append(num)
printable = set(check)
print(len(printable))
