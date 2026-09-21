class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n=[]
        for i in s:
            if i.isalnum():
                n.append(i.lower())
        return n==n[::-1]