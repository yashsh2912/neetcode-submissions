class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_copy = set(nums)
        return not len(nums_copy) == len(nums) 
        