class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #seen_s={}
        #for i in s:
        #    seen_s=seen_s.get(i,0)+1
        #print(seen_s)
        return sorted(s) == sorted(t)