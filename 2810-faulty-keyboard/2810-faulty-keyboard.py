class Solution:
    def finalString(self, s: str) -> str:
        st=list(s)
        res=[]
        for i in st:
            if i in ('i','I'):
                res=res[::-1]
            else:
                res.append(i)

        return "".join(res)

