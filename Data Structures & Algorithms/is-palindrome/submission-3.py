class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""

        for i in s:
            i = i.lower()
            if i.isalnum():
                s_clean += i

        if s_clean == s_clean[::-1]: return True
        return False