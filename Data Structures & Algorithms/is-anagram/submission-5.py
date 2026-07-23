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

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT