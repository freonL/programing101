# rotate 2D-array / Matrix 90 degree clockwise
# input: 2D-array with size n*n, which  0 < n < 10000
# output: rotated 2D-array with size n*n

def rotateMatrix( arr):
    n = len(arr)
    # transpose row to column
    for i in range(0,n):
        for j in range(i,n):
            arr[j][i], arr[i][j] = arr[i][j], arr[j][i]
    
    # flip columns
    mid = int(n / 2)
    for i in range(0,n):
        for j in range(0,mid):
            arr[i][j], arr[i][n-1- j] =  arr[i][n-1- j], arr[i][j]
    
    return arr