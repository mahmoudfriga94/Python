
def OrderedSubstring(string):
    str = ""
    list = []
    for i in range(1,len(string)):
        if i == len(string)-1:
            str += string[i - 1]
            str += string[i]
            list.append(str)
        if ord(string[i-1]) < ord(string[i]):
            str += string[i-1]
        else:
            str += string[i-1]
            list.append(str)
            str =""
    max = 0
    for j in range(0,len(list)):
        if len(list[max]) >= len(list[j]):
            max = max
        else:
            max = j
    print(list[max])

OrderedSubstring("deacedabcdtrabhfmnhddengfabcdefgh")