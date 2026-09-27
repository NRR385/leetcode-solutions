class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st=list(s)
        step=2*k
        for i in range(0,len(st),step):
            l=i
            r=min(i+k-1,len(st)-1)
            while l<r:
                st[l],st[r]=st[r],st[l]
                l+=1
                r-=1

        return "".join(st)

