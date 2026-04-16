def smallest(n:float, m:float) -> float:
    if n<m:
        return n #this statement is evaluated for neither calls.
    else:
        return m
first = smallest(3,2)  #The value of first is 2
second = smallest(2,2) #The value of second is 2. This is a reasonable result because between the two numbers, the lowest value is still 2.
print()

def function2(a:int, b:int, c:int) -> int:
    if a>b and a>c:
        return a-b #a call to this function will evaluate this statement whenever a is the largest integer in the list of parameters
    elif b>c:
        return b+c #a call to this function will evaluate this statement when b is the largest integer in the list of parameters
    else:
        return 2*c #a call to this function will evaluate to this statement if c is the largest integer in the list
answer1 = function2(3, 2, 1) #answer1 = 1
answer2 = function2(2, 3, 1) #answer2 = 4
answer3 = function2(2,1 ,3) #answer3 = 6
print()
