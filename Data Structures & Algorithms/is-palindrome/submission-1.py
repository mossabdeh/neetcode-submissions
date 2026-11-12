class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(c for c in s.lower() if c.isalnum())
        return c == c[::-1]
        