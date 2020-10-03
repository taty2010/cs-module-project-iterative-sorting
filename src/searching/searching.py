def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lhs = 0
    rhs = len(arr) -1
    while lhs <= rhs:
        mid = (lhs + rhs) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] > target:
            rhs = mid - 1
        else:
            lhs = mid + 1
    return -1

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# def test_binary_search(arr1, -8):
