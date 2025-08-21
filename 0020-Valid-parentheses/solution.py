class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack or pairs[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False