start = 2000
end = 3200
number = []
cin = True
while(cin==True):
    for i in range(start,end):
        if(i%7==0 and i%5!=0):
            number.append(i)
    print(number)
    answer = input("do you want to read again? Yes/No \n").lower()
    if(answer == "yes"):
        cin = True
    elif(answer == "no"):
        cin = False
    else:
        print('error')
print("thank you for reading")
