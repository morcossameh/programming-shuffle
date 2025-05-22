# Problem: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
            
        # init hash table to hold matching parentheses
        matching = {')': '(', '}': '{', ']': '['}

        # init stack
        stack = []

        # loop string and check parentheses
        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching.keys():
                if stack == [] or matching[char] != stack.pop():
                    return False
            else:
                return False

        # return result
        return stack == []
