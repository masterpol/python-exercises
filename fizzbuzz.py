"""
Problem: FizzBuzz

Write a function called fizzbuzz that takes a positive integer n as input and returns a list of strings from 1 to n.
However, there are three additional rules:

For numbers that are multiples of 3, the list should contain "Fizz" instead of the number.
For numbers that are multiples of 5, the list should contain "Buzz" instead of the number.
For numbers that are multiples of both 3 and 5, the list should contain "FizzBuzz" instead of the number.

The input n will be a positive integer (n > 0).
"""

def fizzbuzz(n: int) -> list[str]:
    return ["Fizz" if x % 3 == 0 and x % 5 != 0 else "Buzz" if x % 5 == 0 and x % 3 != 0 else "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else f"{x}" for x in range(1, n + 1)]
    
print(fizzbuzz(15))
# Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
