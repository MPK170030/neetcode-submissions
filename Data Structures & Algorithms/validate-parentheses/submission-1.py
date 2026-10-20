class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'}': '{',')': '(',']': '['}
        stack = []

        for char in s:
            if char in set(['}',')',']']):
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == hash_map[char]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        
        return len(stack) == 0