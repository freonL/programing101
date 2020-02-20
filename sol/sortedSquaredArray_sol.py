# O(n) time complexity
# input: sorted array which contain random integer from -X to Y; 
#   i.e.: [-6, -4 , -2, 0, 1 ,3, 5]
# output: sorted array
#   i.e.: [0, 1, 4, 9, 16, 25, 36] 


def sortedSquaredArray(arr):
    n = len(arr)
    if n == 0:
        return None
    out = list()
    for i in range(0,n):
        out.append(0)

    l_ptr = 0
    r_ptr = n - 1

    for i in range(r_ptr, -1, -1):
        if abs(arr[l_ptr]) > arr[r_ptr]:
            out[i] = arr[l_ptr] * arr[l_ptr]
            l_ptr += 1
        else:
            out[i] = arr[r_ptr] * arr[r_ptr]
            r_ptr -= 1
    
    return out
