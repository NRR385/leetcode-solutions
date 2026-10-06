class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=0
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    res+=1
        res += len(stack)
        return res