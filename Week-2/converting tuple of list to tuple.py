#python program to flatten tuple of list to tuple
tl=([5,6],[4])
print("Given tuple of lists:",tl)
t=[]
for i in tl:
    for j in i:
        t.append(j)
res=tuple(t)
print("Flatten tuple:",res)
