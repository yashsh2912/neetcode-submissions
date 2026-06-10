class Solution:
    def isValid(self, s: str) -> bool:
        parn = {'}':'{' , ']':'[',')':'('}
        stack = []
        for char in s:
            if char in parn:
                if stack and stack[-1] == parn[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack 
        