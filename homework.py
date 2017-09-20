start = 2000
end = 3200
number = []
for i in range(start,end):
    if(i%7==0 and i%5!=0):
        number.append(i)
    else:
        continue
print(number)
