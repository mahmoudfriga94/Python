
def GenerateArray(length,start):
    list = []
    num = start-1
    for i in range(0,length):
        num += 1
        list.append(num)
    print(list)

GenerateArray(7,2)