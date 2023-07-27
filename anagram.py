"""
Problem: Anagram Checker

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, "listen" is an anagram of "silent".

Write a function called is_anagram that takes in two strings as input and returns True if the two strings are anagrams of each other, and False otherwise. The function should be case-insensitive and should ignore spaces.
"""

def is_anagram(str1, str2):
    first_list = list(str1.lower().replace(" ", ""))
    second_list = list(str2.lower().replace(" ", ""))

    if len(first_list) != len(second_list):
        return False
        
    freq = {}
    for char in first_list:
         freq[char] = freq.get(char, 0) + 1

    return all([chart in freq and freq[chart] == second_list.count(chart) for chart in second_list])
    
print(is_anagram("Listen", "Silent"))  # Output: True
print(is_anagram("hello", "world"))   # Output: False
print(is_anagram("Eleven plus two", "Twelve plus one"))  # Output: True
print(is_anagram("Astronomer", "Moon starer"))  # Output: True
