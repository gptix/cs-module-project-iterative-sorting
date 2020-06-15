def linear_search(arr, target):
    
    if arr == None or target == None:
        return None

    found = -1
    idx = -1

    for cell in arr:
        idx += 1
        if cell == target:
            found = idx

    return found  # -1 if not not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    left_end = 0
    right_end = len(arr)-1
    midpoint = 0

    while left_end <= right_end:
        midpoint = (right_end + left_end) // 2
        if arr[midpoint] < target:
            left_end = midpoint + 1

        elif arr[midpoint] > target:
            right_end = midpoint - 1

        else:
            return midpoint

    return -1  # not found
