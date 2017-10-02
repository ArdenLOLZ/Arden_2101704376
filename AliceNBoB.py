N = input()
numbers = int(N)
if numbers %3 == 0 or numbers ==1:
    print("Alice")
elif numbers %2 == 0:
    print("Bob")
else:
    print(None)
