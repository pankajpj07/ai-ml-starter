"""
Test cases for day2 leetcode
"""

import pytest
from day2_leetcode import two_sum, is_palindrome, roman_to_int, removeElement


"""
Testing two_sum function
"""
@pytest.mark.parametrize("nums,target,expected", [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ([2,4,11,3], 6, [0,1])])

def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


"""
Testing is_palindrome function
"""

@pytest.mark.parametrize("x,expected",[
    (121,True),
    (-121,False),
    (10,False),
    (12321,True),
    (1234567890,False),
    (0,True),
    (1,True),
    (1000021,False),
])
def test_is_palindrome(x,expected):
    assert is_palindrome(x) == expected

"""
Testing roman_to_int function
"""

@pytest.mark.parametrize("s,expected",[
    ("III",3),
    ("IV",4),
    ("IX",9),
    ("LVIII",58),
    ("MCMXCIV",1994),
])
def test_roman_to_int(s,expected):
    assert roman_to_int(s) == expected


@pytest.mark.parametrize("nums,val,expected",[
    ([3,2,2,3],3,2),
    ([0,1,2,2,3,0,4,2],2,5),
    ([1],1,0),
    ([],1,0),
    ([1,2,3,4,5],6,5),
])
def test_removeElement(nums,val,expected):
    assert removeElement(nums,val) == expected