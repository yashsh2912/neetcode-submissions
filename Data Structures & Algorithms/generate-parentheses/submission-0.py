class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def dfs(openCount, closeCount):
            if openCount == closeCount == n:
                res.append(''.join(string))
                return 

            if openCount < n:
                string.append('(')
                dfs(openCount + 1, closeCount)
                string.pop()
            if closeCount < openCount:
                string.append(')')
                dfs(openCount, closeCount + 1)
                string.pop()
        dfs(0,0)
        return res
        