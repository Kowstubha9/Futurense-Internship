#python program to print the index of common elements present in the given tuples
t1=([1,2],[3,4],[5,6],[7,8])
t2=([1,3],[3,4],[5,6],[9,8])
l=[]
for i in t1:
    for j in t2:
        if(i==j):
            x=t1.index(i)
            l.append(x)
print("The common elements are present at the indices:",tuple(l))
