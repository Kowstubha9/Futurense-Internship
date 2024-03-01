#Finding simple interest
p=int(input("Enter principal:"))
t=int(input("Enter time:"))
r=int(input("Enter rate of interest:"))
SI=(p*t*r)/100
print(SI)

#Finding compound interest
p=float(input("Enter principal:"))
t=float(input("Enter time:"))
r=float(input("Enter rate of interest:"))
n=float(input("Enter number of times interest is compounded per year:"))
CI=(p*((1+r/n)**(n*t)))-p
print(CI)
