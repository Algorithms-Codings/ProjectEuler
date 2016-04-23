

f=lambda n:sorted(str(n))

n=99999
while(not(f(n)==f(n*2)==f(n*3)==f(n*4)==f(n*5)==f(n*6))):
    n=n+9

print(n)
