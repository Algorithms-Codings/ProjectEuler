
x=''
i=1
while(len(x)<=1000000):
   x=x+str(i)
   i=i+1

j=1
prod=1
while (j<=1000000):
    prod=prod* int(x[j-1])
    j=j*10
    
print(prod)
