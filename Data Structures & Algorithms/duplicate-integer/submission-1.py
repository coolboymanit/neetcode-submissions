class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_counter = set(nums)

        if (len(set_counter) == len(nums)):
            return False

        return True
            