class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        srt=sorted(heights)
        res=0
        for i in range(len(heights)):
            if heights[i]==srt[i]:
                continue
            res+=1
        return res