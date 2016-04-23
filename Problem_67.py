lines= [list(line.strip('\n').split()) for line in open('p067_triangle.txt')]


i=len(lines)-1
while(i>0):
    j=i
    while(j>0):
        if(int(lines[i][j])>int(lines[i][j-1])):
            num=int(lines[i][j])
            
            lines[i-1][j-1]=num +int(lines[i-1][j-1])
        else:
            num=int(lines[i][j-1])
            lines[i-1][j-1]=num + int(lines[i-1][j-1])
        j=j-1
    i=i-1

print(lines[0][0])
