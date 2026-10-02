class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False

            count[char] -= 1

        for value in count.values():
            if value != 0:
                return False

        return True
        