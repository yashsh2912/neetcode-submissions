class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "qprs", "8": "tuv", "9": "wxyz" }

        def bt(i, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            
            for c in digitToChar[digits[i]]:
                bt(i + 1, currString + c)

        if digits:
            bt(0, '')

        return res
        