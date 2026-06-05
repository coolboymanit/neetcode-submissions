class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        first = []
        count = 0

        for n in s:
            if n-1 not in s:
                first += [n]

        print(f"Set: {s}, First: {first}")
        

        for item in first:
            c = 0
            curr = item
            while curr in s:
                c += 1
                curr += 1
            if c > count: 
                count = c

        return count