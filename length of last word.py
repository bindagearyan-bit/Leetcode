class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=s.strip()
        w=c.split(" ")

        return len(w[-1])
        
