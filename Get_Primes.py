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
    return deque(r)

def isprime(n):
    for i in range(2,int(sqrt(n))+1):
                   if(n%i==0):
                       return 0
                   else:
                       return 1
        
                   
primes=get_primes(10000)

