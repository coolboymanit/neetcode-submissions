from collections import OrderedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1

        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        l = list(sorted_dict)
        f = []

        for i in range(k):
            f.append(l[i])

        return f