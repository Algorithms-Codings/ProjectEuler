import itertools
from math import sqrt
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
                   if(n%i==0):
                       return False
    else:
       return True

digits = [int(x) for x in str(1234567)]
n_digits = len(digits)
n_power = n_digits - 1
permutations = itertools.permutations(digits)
s=[sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]
#print(s)
#print(len(s))
i=0
maxnum=0
while(i<len(s)):
    if((s[i]%2==0) or (s[i]%5==0) or (s[i]%3==0) or (s[i]%7==0)):
        s.remove(s[i])
        i=i-1
    elif (isprime(s[i])==False):
        s.remove(s[i])
        i=i-1
    elif (maxnum<s[i]):
        maxnum=s[i]
    i=i+1
print(maxnum)
#print(s)
