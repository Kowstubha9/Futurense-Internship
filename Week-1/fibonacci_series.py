#printing fibonacci series upto given position
def fib(n):
    n1,n2=1,1
    print(n1)
    print(n2)
    for i in range(2,n):
        nth=n1+n2
        print(nth)
        n1=n2
        n2=nth
x=int(input("Enter the number:"))
print("Fibonacci series:")
fib(x)
