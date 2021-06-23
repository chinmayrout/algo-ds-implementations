def bubble(arr):
    n = len(arr)

    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i], arr[i+1]

    
    return arr


# Driver Code
arr = [1, 4, 2, 6, 9, 0, -1]
print(bubble(arr))