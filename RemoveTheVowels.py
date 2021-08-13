


def RemoveTheVowels(str):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for s in str:
        if s in vowels:
            str = str.replace(s, "")
    return str

str = "Mobile"
str = RemoveTheVowels(str)
print(str)