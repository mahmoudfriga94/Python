

def ListOfSimilar(list):
    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new

list = [1,2,1,2,3,4,2,4]

new = ListOfSimilar(list)
print(new)

