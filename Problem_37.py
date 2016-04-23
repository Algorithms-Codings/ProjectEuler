from math import sqrt;
from collections import deque;

def get_primes(n):
    

    x=[k for k in range(2,n)  if('2' not in str(k)[1:-1]  and '5' not in str(k)[1:-1] and '0'  not in str(k) and '4' not in str(k) and '6' not in str(k) and '8' not in str(k))]   
    
    #x1=[int(str(x)[i:len(str(x))]) for i in range(0,len(str(x)))]
    #x2=[int(str(x)[0:len(str(x))-i]) for i in range(0,len(str(x)))]
    
    #r=list(range(2,n))
    #v=range(2,n)
    r=x
    for i in range(2,int(sqrt(n))+1):
            for k in range(i*i,n+1,i):
                if(k in r):
                    r.remove(k)
    res=0
    #print(r)
    count=0
    for x in r:
            #print(r)
            bPrime=True
            if('1' not in str(x)[0]  and '1' not in str(x)[-1] and '9' not in str(x)[0]  and '9' not in str(x)[-1] and '2' not in str(x)[1:-1]  and '5' not in str(x)[1:-1] and '0'  not in str(x) and '4' not in str(x) and '6' not in str(x) and '8' not in str(x) and len(str(x))>1):
                for i in range(0,len(str(x))):
                    #print("[", int(str(x)[i:len(str(x))]),"]")
                    #print("[",int(str(x)[0:len(str(x))-i]),"]")
                    if((int(str(x)[i:len(str(x))]) not in r) or (int(str(x)[0:len(str(x))-i])  not in r)):
                        bPrime=False
                        
                        break
                if(bPrime==True):
                    count=count+1
                    res=res+x
                if(count==11):
                    break
    return res
                
print("Res:" , get_primes(1000000))
