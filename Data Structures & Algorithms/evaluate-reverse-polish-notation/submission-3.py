class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if not tokens: return 0
        for op in tokens:
            if op == '+':
                a,b = stack.pop(), stack.pop()
                stack.append(b+a)
            elif op == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif op == '*':
                a,b = stack.pop(), stack.pop()
                stack.append(b*a)
            elif op == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(op))
        return stack[0]

