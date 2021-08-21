
def DivideString(string):
    list = []
    if len(string)%2 == 0:
        string1 = ""
        for i in range(0,len(string)//2):
            string1 = string1+string[i]
        list.append(string1)
        string2 = ""
        for i in range((len(string)//2),len(string)):
            string2 = string2+string[i]
        list.append(string2)
    else:
        string1 = ""
        for i in range(0, (len(string)+1) // 2):
            string1 = string1 + string[i]
        list.append(string1)
        string2 = ""
        for i in range(((len(string)+1) // 2), len(string)):
            string2 = string2 + string[i]
        list.append(string2)
    return list

def NewString(str1,str2):
    list1 = DivideString(str1)
    list2 = DivideString(str2)
    print(list1[0]+list2[0]+list1[1]+list2[1])

str1 = "ahmedhamdy"
str2 = "rashasaad"
NewString(str1,str2)