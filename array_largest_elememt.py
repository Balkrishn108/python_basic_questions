def find_largest_elememt(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element>largest_element:
            largest_element = element
    return largest_element

my_array = [10,20,25,35]
result = find_largest_elememt(my_array)
print(f"Largest element is {result}")