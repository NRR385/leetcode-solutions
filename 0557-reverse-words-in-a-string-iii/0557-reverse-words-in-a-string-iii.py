class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split()
        res=[]
        for i in st:
            res.append(i[::-1])
        return ' '.join(res)