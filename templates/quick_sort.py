def qsort(nums: List[int]) -> None:
    def qsort_helper(nums: List[int], l: int, r: int) -> None:
        if l >= r: return

        p = partition(nums, l, r)
        qsort_helper(nums, l, p - 1)
        qsort_helper(nums, p + 1, r)

    def partition(nums: List[int], left: int, right: int) -> int:
        fill = left
        pivot = nums[right]
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        
        nums[fill], nums[right] = nums[right], nums[fill]
        
        return fill
        
    qsort_helper(nums, 0, len(nums) - 1)