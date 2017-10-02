line = input("input set pattern :")
length = len(line)
order = list(line)
a = 1
b = 2
c = 3
hacked = False
print("The pattern list:")
print(order)
def switch1():
    global a,b
    temp = 0
    temp = a
    a = b
    b = temp
def switch2():
    global b,c
    temp = 0
    temp = b
    b = c
    c = temp
def switch3():
    global a,c
    temp = 0
    temp = c
    c = a
    a = temp
for x in range (0,length-1):
    if order[length-1-x].lower() == 'a':
        switch1()
    elif order[length-1-x].lower() == 'b':
        switch2()
    elif order[length-1-x].lower() == 'c':
        switch3()
    else:
        hacked = True
if hacked == False:
    print('It is in cup ' + str(a))
else:
    print('error! unidentified pattern')
