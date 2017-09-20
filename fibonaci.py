x = [0,1]
for i in range(1,9):
    store = x[i-1] + x[i]
    x.append(store)
print(x)
