class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        st=list(s)
        v="aeiouAEIOU"
        while l<r:
            if(st[l] in v):
                if(st[r] in v):
                    st[l],st[r]=st[r],st[l]
                    l+=1
                    r-=1
                else:
                    r-=1
            else:
                l+=1
        return "".join(st)
