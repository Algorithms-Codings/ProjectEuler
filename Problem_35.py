from math import sqrt
def circularNum(num):
    r=(str(num).strip())
    tot=0
    l=[tot+ int(r[-i:]+r[:-i]) for i in range(0,len(r))]
    return(l)


def get_primes(n):
    

    r=[k for k in range(2,n)  if('2'  not in str(k) and '0'  not in str(k) and '4' not in str(k) and '6' not in str(k) and '8' not in str(k) or len(str(k))==1)]
    
    
    
    for i in range(2,int(sqrt(n))+1):
            for k in range(i*i,n+1,i):
                if(k in r):
                    r.remove(k)
    
    
    return r


n=1000000
primes=get_primes(n)
#print(primes)
tot=0
for p in primes:
    #print(p,circularNum(p))
    s=set(circularNum(p))
    if(s.issubset(set(primes))):
        #print(p,circularNum(p))
        tot=tot+len(s)
        primes=list(set(primes).difference(s))
    else:
        primes=list(set(primes).difference(s))
        
print(tot)



