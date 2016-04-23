from math import sqrt
def isPentagonal(i):
    penTest = (sqrt(1+24*i) + 1.0) / 6.0;
    return penTest == (penTest // 1)

    
x=145
while(True):
    x=x+1
    result=x*((x*2)-1)
    if(isPentagonal(result)):
        break

print(result)

