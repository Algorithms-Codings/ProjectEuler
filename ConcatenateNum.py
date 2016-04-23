def concatenateNum(n):
    #k=[[str(i)[k] for k in range(0,len(str(i)))] for i in n]
    k=n
    result=""
    for i in range(0,len(k)-1):
        for j in range(i+1,len(k)):
            #print(k[i],k[j])
            if(GreaterDigit(0,k[i],k[j])):
                res=k[i]
                #print("res:" , res)
                #print("k:",k)
            else:
                res=k[j]
                #print("res1:",res)                
                k[j]=k[i]
                k[i]=res
                #print("k:",k)
    for i in k:
        result=result+str(i)
    return result
        
def GreaterDigit(d,num1,num2):
    if d==len(str(num1)):
        return True
    elif d==len(str(num2)):
        return False
    elif int(str(num1)[d])>int(str(num2)[d]):
        return True
    elif int(str(num1)[d])<int(str(num2)[d]):
        return False
    elif int(str(num1)[d])==int(str(num2)[d]):
        d=d+1
        val=GreaterDigit(d,num1,num2)
        return val

print(concatenateNum([9,9179,8945,918]))        
        
        
