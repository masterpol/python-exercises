"""
Problem: Merge Intervals

Given a list of intervals, merge any overlapping intervals. The input list is sorted in ascending order based on the start of each interval.

Write a function called merge_intervals that takes a list of intervals as input and returns a new list of merged intervals.

Each interval is represented as a list containing two integers [start, end], where start is the start of the interval, and end is the end of the interval.
"""

from typing import List
from functools import reduce

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    return reduce(lambda acc, value: [*acc, value] if len(acc) == 0 or min(acc[-1]) < min(value) and max(acc[-1]) < min(value) else [*acc[:-1], [min(acc[-1] + value), max(acc[-1] + value)]], intervals, [])
    

print(merge_intervals([[1, 4], [0, 2], [3, 5]])) # Output: [[0, 5]]

print(merge_intervals([[1, 3], [2, 4], [5, 7], [6, 8]])) # Output: [[1, 4], [5, 8]]

print(merge_intervals([[1, 10], [11, 20], [21, 30]])) # Output: [[1, 10], [11, 20], [21, 30]]

print(merge_intervals([[1, 5], [6, 8], [9, 12]])) # Output: [[1, 5], [6, 8], [9, 12]]

print(merge_intervals([[1, 5], [2, 6], [3, 7]])) # Output: [[1, 7]]
