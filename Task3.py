def smallest(n:float, m:float) -> float:
    if n<m:
        return n #this statement is evaluated for neither calls.
    else:
        return m
first = smallest(3,2)  #The value of first is 2
second = smallest(2,2) #The value of second is 2. This is a reasonable result because between the two numbers, the lowest value is still 2.
print()]
