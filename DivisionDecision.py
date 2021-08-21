
def DivisionDecision(num):
    if(num%3 == 0 and num%5 == 0):
        print("FizzBuzz")
    elif(num%5 == 0):
        print("buzz")
    elif(num%3 == 0):
        print("Fizz")
    else:
        print("Number is not divisible by 3 or 5")

DivisionDecision(9)
DivisionDecision(10)
DivisionDecision(15)
DivisionDecision(4)