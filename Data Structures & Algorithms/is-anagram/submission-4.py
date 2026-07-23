class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1, map2 = {},{}
        for ch in range(len(s)):
            if s[ch] in map1:
                map1[s[ch]] += 1
            else:
                map1[s[ch]] = 1
            if t[ch] in map2:
                map2[t[ch]] += 1
            else:
                map2[t[ch]] = 1
        
        return map1 == map2