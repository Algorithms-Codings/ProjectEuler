
from math import sqrt;
from collections import deque;
def get_primes(n):
    

    r=list(range(n))
    r.remove(0)
    r.remove(1)
    for i in range(2,int(sqrt(n))+1):
            for k in range(i*i,n+1,i):
                if(k in r):
                    r.remove(k)
    return r

def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
                   if(n%i==0):
                       return False
    else:
       return True

n = 1000000
x=5000
primes = get_primes(x)
#print(primes)
maxsum=0
maxcount=0
totsums=[(i,j,sum(primes[i:j])) for i in range(0,len(primes)) for j in range(i+1,len(primes)+1) if(is_prime(sum(primes[i:j])) and sum(primes[i:j])<n)]
#print(totsums)
#count=[j-i for i in range(0,len(primes)) for j in range(i+1,len(primes)+1)  if(is_prime(sum(primes[i:j])) and sum(primes[i:j])<n)]
#sumrange=[(i,j) for i in range(0,len(primes)) for j in range(i+1,len(primes)+1)  if(is_prime(sum(primes[i:j])) and sum(primes[i:j])<n)]
for i in range(0,len(totsums)):
    if(maxsum<totsums[i][2]) and maxcount<(totsums[i][1]-totsums[i][0]):
        maxsum=totsums[i][2]
        maxcount=(totsums[i][1]-totsums[i][0])
        r=primes[totsums[i][0]:totsums[i][1]]

print(maxsum)
print(maxcount)
print(r)

        
        
        
