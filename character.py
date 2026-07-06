string=input("Please enter your own string:")
character=input("Please enter your own character:")
if (len(character))==1:
    i=0
    count=0
    while (i<len(string)):
        if (string [i]==character):
            count=count+1
        i=i+1
    print("The string",string,"has the character",count,"times.")
else:
    print("Invalid")
    