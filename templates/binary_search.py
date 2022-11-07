# If the target exists, returns its leftmost index.
# Else, returns the index of where it should be.
"""
·  check whether the target exists. 
    arr[binarySearch(arr, 2)] == 2

·  find the leftmost index of the target if it exists. 
    binarySearch(arr, 3) = 2
    binarySearch(arr, 9) = 6

·  find the index of where the target should be if it doesn't exist. 
    binarySearch(arr, 4) = 5
    binarySearch(arr, -5) = 0
    binarySearch(arr, 100) = 7
"""

def binarySearch(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r :
        m = (r - l) // 2 + l
        if target > nums[m]:
            l = m + 1
        else: 
            r = m
    return l