from typing import List

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Input: nums = [1, 2, 3, 3] -> Output: true

nums = [1, 2, 3, 4]
def has_duplicate(nums: List[int]):
    my_map = {}
    for i in nums:
        if i in my_map: return  True
        else:
            my_map[i] = True

    return False

print(has_duplicate(nums))