#Checking whether the given number is prime number or not
def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("Not prime")
            break
    else:
        print("prime")
x=int(input("Enter number:"))       
prime(x)
