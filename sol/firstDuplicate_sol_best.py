# Find the first duplicate in list of numbers (ls)
# the numbers are between 1 and n, where n is the length or list
# if the list not valid or there is no duplicate, it will return -1

def firstDuplicate(ls):
    n = len(ls)
    if n < 2 :
        return -1
    
    for i in ls:
        if abs(i) > n :
            return -1

        if ls[abs(i)-1] < 0 :
            return abs(i)
        
        ls[abs(i)-1] *= -1 
        
    return -1

