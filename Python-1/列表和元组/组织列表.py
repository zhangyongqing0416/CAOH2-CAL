lst7=[78,89,23,73,73,65,38,49,74,33]
print(sorted(lst7,reverse=False))
print(lst7)
for i in range(1,5,1):
    print(i,end=',')
lst10=[]
for i in range(1,10):
    lst10.append(i)
del lst10[:]
for i in range(1,10):
    lst10.append(i**2)
print(lst10)
