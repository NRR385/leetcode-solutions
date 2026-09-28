class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):
            return False
        str=s+s
        if(str.find(goal)!=-1):
            return True  
        return False