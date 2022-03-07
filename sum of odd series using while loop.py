n=int(input("enter the number"))
sum=0
i=1
while i<=n:
        sum=sum+i
        if i!=n:
          print(f"{i}+",end="")
        else:
            print(f"{i}=",end="")
        i=i+2
print(sum)
