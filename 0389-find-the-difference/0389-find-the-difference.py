class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=list(s)
        y=list(t)
        x.sort()
        y.sort()
        for i in range(len(s)):
            if x[i]!=y[i]:
                return y[i]
        return y[-1]