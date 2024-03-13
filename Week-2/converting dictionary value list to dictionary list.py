#python program to convert dictonary value list to dictionary list
d1=[{"student_id":[15,27]},{"Name":["Ram","Kavya"]}]
l=[]
for i in range(len(d1)):
    a={}
    l.append(a)
k = 0
for i in d1:
    for key, val in i.items(): 
        for j in val:
            l[k][key] = j
            k += 1
        k = 0
print(l)
