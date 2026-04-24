from typing import List

# Solution 1: Sort the array first
def longest_consecutive_sequence_sorted(nums: List[int]) -> int:
    if len(nums) == 0: return 0
    #if we sort the numbers first, then all the consecutive values will appear next to each other
    nums.sort()
    res = 0
    curr, streak = nums[0], 0
    i = 0
    while i < len(nums):
        # reset the streak if the next consecutive value is not matched
        if curr != nums[i]:
            streak = 0
            curr = nums[i]
        # move the index until we found the value is not duplicated
        while i < len(nums) and nums[i] == curr:
            i += 1
        streak += 1
        curr += 1
        res = max(res, streak)
    return res

def longest_consecutive_sequence_hash_set(nums: List[int]) -> int:
    res = 0
    nums_set = set(nums)
    for n in nums:
        # if n - 1 not in the nums set mean it's the start of the consecutive values
        if n - 1 not in nums_set:
            #start counting
            streak = 0
            curr = n
            while curr in nums_set:
                streak += 1
                curr += 1
            res = max(streak, res)
    return res

test_input = [0,1,2 ,3, 4]
print(longest_consecutive_sequence_sorted(test_input))
print(longest_consecutive_sequence_hash_set(test_input))
