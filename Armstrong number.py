#Checking whether the given number is armstrong number or not
def armstrong(n):
    l=list(str(n))
    a=[]
    for i in range(len(l)):
        a.append(int(l[i])**len(l))
    if(n==sum(a)):
        print("Armstrong number")
    else:
        print("Not armstrong number")
x=int(input("Enter number:"))
armstrong(x)
