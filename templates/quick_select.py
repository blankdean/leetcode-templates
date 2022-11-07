# QuickSelect: O(n) average, O(n²) worst
# Heap: O(n log k)
def findKthLargest(self, nums: List[int], k: int) -> int:
    def qselect(nums: List[int], l: int, r: int, k: int) -> None:
        p = partition(nums, l, r)
        
        if p < k: 
            return qselect(nums, p + 1, r, k)
        if p > k: 
            return qselect(nums, l, p - 1, k)
        
        return nums[p]

    def partition(nums: List[int], left: int, right: int) -> int:
        fill = left
        pivot = nums[right]
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        
        nums[fill], nums[right] = nums[right], nums[fill]
        
        return fill

    return qselect(nums, 0, len(nums) - 1, len(nums) - k)
    