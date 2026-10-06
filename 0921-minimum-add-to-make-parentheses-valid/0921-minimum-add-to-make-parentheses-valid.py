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





        '''
        r1=[]
        r2=[]
        r1_size=0
        r2_size=0
        for i in s:
            if i=='(':
                r1.append(i)
                r1_size+=1
            else:
                r2.append(i)
                r2_size+=1
        if(r1_size==r2_size):
            return 0
        else:
            return abs(r1_size-r2_size)
        '''