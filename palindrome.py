x = '"redivider"'
word = list(x)
length = len(word)
check = True
print(x.title() +" is a palindrome?")
for i in range (0 , length):
    if(word[i]!= word[length-1-i]):
        check = False
    else:
        continue
if(check == True):
    print("Yes, this word is a palindrome")
else:
    print("No, this word is not a palindrome")
