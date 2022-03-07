n=int(input("enter the number"))
a=0
b=1
i=0
while i<n:
    if i<=1:
        fib=i
    else:
        fib=a+b
        a=b
        b=fib
    i=i+1
    print(f"{fib},",end=" ")
