def pentagon(i):
    return (i*(3*i-1))/2
Pn=[(i*(3*i-1))/2 for i in range(1,3000)]
#print(Pn)
for i in range(0,len(Pn)):
    for j in range(i+1,len(Pn)-1):
        if (((Pn[i]+Pn[j]) in Pn) and ((Pn[j]-Pn[i]) in Pn)):
            print(Pn[j]-Pn[i])

