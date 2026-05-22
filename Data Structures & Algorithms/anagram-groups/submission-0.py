class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = sorted(strs)

        final = []
        counted = set()
        for i in range(len(strs)):
            if i in counted: continue
            s = sorted(strs[i])
            l = [strs[i]]
            for j in range(len(strs)):
                if j in counted or i == j: continue
                compare_s = sorted(strs[j])

                if s == compare_s:
                    l.append(strs[j])
                    counted.add(j)
            
            final.append(l)

        return final
