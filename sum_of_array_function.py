def sum_array(arr):
    total = 0
    for element in arr:
        total += element
    return total

arr = [1,2,3,4,5]
result = sum_array(arr)
print(result)