class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char = {}
        for i in s:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        for j in t:
            if j in char:
                char[j] -= 1
                if char[j] == 0:
                    char.pop(j)
        if char :
            return False
        else :
            return True