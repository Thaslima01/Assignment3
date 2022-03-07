n=int(input("enter the number"))
a=0
b=1
for i in range(0,n):
    if i<=1:
       fib=i
    else:
       fib=a+b
       a=b
       b=fib
    print(f"{fib},",end=" ")
    
