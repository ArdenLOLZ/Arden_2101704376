name = input("input the name :\n")
length = len(name)
short = ""
for a in range(0,length):
    if(name[a]==name[a].upper() and name[a]!= "-"):
        short += name[a]

print(short)
