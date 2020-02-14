# Find the first duplicate in list of numbers (ls)
# the numbers are between 1 and n, where n is the length or list
# if the list not valid or there is no duplicate, it will return -1

def firstDuplicate(ls):
    n = len(ls)
    if n < 2 :
        return -1

    duplicateIndex = n
    for i in range (n-1):
        if ls[i] > n:
            return -1
        for j in range(i+1, n):
            if ls[i] == ls[j]:
                if j < duplicateIndex:
                    duplicateIndex = j
    if duplicateIndex == n:
        return -1
    return ls[duplicateIndex] 

