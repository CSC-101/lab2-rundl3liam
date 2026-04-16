def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) #on call one test = false, on call two test = true
    if test: #this check prevents trying to pull a value from a list of index longer than the length of the list, which would break the code
        return L[idx]
    else:
        return None
first = checked_access([1, 0, 1], 9) #first = none
second = checked_access([1, 0, 1], 2) #second = 1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:#this statement is evaluated for the first call
        result = len(L[0]) + len(L[1]) + len(L[2]) #the values being added are the lengths of the first three words in the first list
    elif len(L) > 1: #this statement is evaluated for the third call
        result = len(L[0]) + len(L[1]) #the values being added are the lengths of the two words in the list
    elif len(L) > 0: #this statement is evaluated for the second call
        result = len(L[0]) #the values being added are just the length of the characters in the list
    else:
        result = 0
    return result
first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L
words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
#the value of words is ["this", "is", "confusing", "code", "AVOID", "SUCH."]
#the value of first is ["this", "is", "confusing", "code", "AVOID", "SUCH."]
#the value of second is ["this", "is", "confusing", "code", "AVOID", "SUCH."]
#The append(other.upper()) command adds the value in the other parameter of each call to the list in the parameter at the end of the list in all uppercase font
print()