#python program to convert list of dictioanry to tuple of list
l=[{"s.no":5,"Name":"Ram"},{"s.no":15,"Name":"Renu"}]
l1=[]
for i in l:
    for j in i:
        a=(i[j])
        l1.append(a)
a=len(l[0])
x=l1[:a]
y=l1[a:]
l2=[x,y]
print(tuple(l2))
