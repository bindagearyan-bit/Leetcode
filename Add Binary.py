class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2)
        d= int(b,2)

        t=c+d

        return bin(t)[2:]

