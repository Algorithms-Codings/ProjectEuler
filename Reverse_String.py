def ReverseString(givenStr):
    Words=givenStr.split(" ")
    RevString=""
    for word in Words:
        if(word==""):
            RevString=RevString +" "
        else:
            RevString=RevString + word[::-1] + " "

    RevString=RevString[0:len(RevString)-1]
    return RevString

print(ReverseString("Hello  World!!!"))
