
dictWord=dict([(0,''),(1,'one'), (2,'two'), (3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),
                (10,'ten'),(11,'eleven'),(12,'twelve'),(13,'thirteen'),(14,'fourteen'),(15,'fifteen'),
                (16,'sixteen'),(17,'seventeen'),(18,'eighteen'),(19,'ninteen'),
                (20,'twenty'),(30,'thirty'),(40,'forty'),(50,'fifty'),(60,'sixty'),(70,'seventy'),(80,'eighty'),(90,'ninety'),
               (100,'hundred'),(1000,'thousand'),('&','and')])


def count_Words(n):
    if(len(str(n))==1):
        #print("<11:",n)
        print(dictWord[n])
        return len(dictWord[n])
    elif((len(str(n))==2) and (n<=20)):
        #print("<20:",n)
        print(dictWord[n])
        return len(dictWord[n])
    elif((len(str(n))==2) and (n>20)):
        #print(">20:",n)
        x1=n-int(str(n)[-1])
        #print(x1)
        x2=int(str(n)[-1])
        
        #print(x2)
        if(x2==0):
            print(dictWord[x1])
            return(len(dictWord[x1]))
        else:
            print(dictWord[x1]," ",dictWord[x2])
            return(len(dictWord[x1])+len(dictWord[x2]))
    elif(len(str(n))==3):
        #print(">100:",n)

        
        x1=count_Words(int(str(n)[0]))

        x2=len(dictWord[100])
       
        if((n%100)==0):
            x3=0
            x4=0
            print(" ",dictWord[100])
        else:
            x3=len(dictWord['&'])
            x4=count_Words(int(str(n)[1:]))
            print(" ",dictWord[100]," ", dictWord['&'] )
        return(x1+x2+x3+x4)
    elif(n==1000):
        return(len(dictWord[1000])+3)


tot=0
for i in range(1,201):
    x=count_Words(i)
    print(i,"=",x)
    tot=tot+x
print(tot)
