class Solution:
    def isPalindrome(self, s: str) -> bool:

        c="".join(char for char in s.lower()if char.isalnum())

        return c==c[::-1]
