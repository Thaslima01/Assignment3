n=int(input("enter the number"))
sum=0
for i in range(1,n+1,2):
        sum=sum+i
        if i!=n:
          print(f"{i}+",end="")
        else:
            print(f"{i}=",end="")
print(sum)
