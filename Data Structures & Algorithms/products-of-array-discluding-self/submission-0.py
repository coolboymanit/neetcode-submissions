class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        # [1, -1, 0, 0, 0]
        # [0, 6, 6, 3, 1]

        prefix_l = [1]
        suffix_l = [1]

        l = len(nums)

        for i in range(1, l):

            prefix_l += [prefix_l[i-1] * nums[i-1]]
        
        print(prefix_l)
        

        for j in range(l - 2, -1, -1):
            suffix_l += [suffix_l[len(suffix_l) - 1] * nums[j + 1]]

        suffix_lr = reversed(suffix_l)

        result = [ x * y for x,y in zip(prefix_l, suffix_lr)]

        return result
