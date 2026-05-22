class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        j = 0
        map = {}

        for i in nums:
            map[i] = map.get(i, 0) + 1

            window = j + 1


            if (len(map) < window):
                return True

            j += 1

        return False
        