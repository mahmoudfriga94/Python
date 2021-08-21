

def FindPos (string,char):
    lst = []
    for i in range (0,len(string)):
        if string[i] == char:
            lst.append(i)
    return lst

string = input("Enter a string: ")
char = input("Enter a character: ")
Pos = []
Pos = FindPos(string,char)
print(Pos)
