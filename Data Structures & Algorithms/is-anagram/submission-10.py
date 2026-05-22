class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = sorted(s)
        set_t = sorted(t)

        if len(s) != len(t): return False

        if len(set_s) == len(set_t):
            for i, j in zip(set_s, set_t):
                print(i, j)
                if i != j:
                    return False

            return True

        return False
