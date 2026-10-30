class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        operators = ["+","-","*","/"]

        for t in tokens:
            if t not in operators:
                tokenStack.append(int(t))
            else:
                secondOperand = tokenStack.pop()
                firstOperand = tokenStack.pop()
                if t == '+':
                    tokenStack.append(firstOperand + secondOperand)
                elif t == '-':
                    tokenStack.append(firstOperand - secondOperand)
                elif t == '*':
                    tokenStack.append(firstOperand * secondOperand)
                else:
                    tokenStack.append(int(firstOperand / secondOperand))
        return tokenStack[0]


        