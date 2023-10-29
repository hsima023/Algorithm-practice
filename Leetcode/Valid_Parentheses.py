#Valid Parentheses

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.
#3.Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        checkSign = []
        
        signs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for ch in s:
            if ch in signs:
                if (len(checkSign) == 0  or checkSign.pop() != signs[ch]):
                    return False
            else:
                checkSign.append(ch)
        
        return not checkSign