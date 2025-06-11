"""
day2 leetcode
Five most common problems:
1. Two Sum
2. Best Time to Buy and Sell Stock
3. Longest Substring Without Repeating Characters
4. Longest Palindromic Substring
5. Merge Two Sorted Lists
"""

from typing import List

# Two Sum (Leetcode 1)

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    seen:dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return []


def is_palindrome(x:int) -> bool:
    """
    Given an integer x, return true if x is a palindrome, or return false otherwise.
    """
    if x<0:
        return False
    return str(x) == str(x)[::-1]


# Roman to Integer (Leetcode 13) IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
def roman_to_int(s:str) -> int:
    """
    Given a roman numeral, convert it to an integer.
    """
    roman_to_int_map = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    total = 0 
    prev_value = 0
    for char in s:
        value = roman_to_int_map[char]
        if value > prev_value:
            total +=value - 2* prev_value
        else:
            total+=value
        prev_value = value
    return total


def removeDuplicates(nums: List[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    """
    result = []
    nums_map = {}
    for i, num in enumerate(nums):
        if not num in nums_map:
            nums_map[num] = i
            result.append(num)
    for i, num in enumerate(result):
        nums[i] = num
    return len(result)