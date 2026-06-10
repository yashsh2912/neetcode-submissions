class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = {}
        for char in s:
            temp[char] = 1 + temp.get(char, 0)
        for char in t:
            if char in temp:
                temp[char] -= 1
                if  temp[char] == 0:
                    temp.pop(char)

        return not temp
