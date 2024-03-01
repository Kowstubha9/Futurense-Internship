#finding prime numbers between given interval
s=int(input("Enter starting of interval:"))
l=int(input("Enter ending of interval:"))
x=[]
for i in range(s,l):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        x.append(i)
print("Prime numbers between",s,"and",l,"are:")      
print(x)
