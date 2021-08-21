

def ReverseString(str):
    string = ""
    for i in range(0,len(str)):
        string += str[len(str)-1-i]
    print(string)

ReverseString("games")

