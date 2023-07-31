"""
Of course! Here's another coding exercise for you:

Problem: Valid Parentheses

Given a string containing only the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:

Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
Note:

An empty string is also considered valid.
Write a function called is_valid_parentheses that takes a string s as input and returns True if the input string is valid,
and False otherwise.
"""

VALID_VALUES = [
    "()",
    "{}",
    "[]"
]

def is_valid_parentheses(s: str) -> bool:
    result = None
    
    while result == None:
        if len(s) == 0:
            result = True
            break
        if not any(substr in s for substr in VALID_VALUES):
            result = False
            break
            
        for substr in VALID_VALUES:
            s = s.replace(substr, "")

    return result

print(is_valid_parentheses("()"))  # Output: True
print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("{[()]}"))  # Output: True
print(is_valid_parentheses("([)]"))  # Output: False
print(is_valid_parentheses("{{{{"))  # Output: False
print(is_valid_parentheses(""))  # Output: True
