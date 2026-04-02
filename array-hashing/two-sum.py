from typing import List


def two_sum(nums: List[int], target):
    my_dict = {}
    for  num, i in enumerate(nums):
        difference =  target - num
        if difference in my_dict:
            return  [i, my_dict.get(difference)]
        my_dict[num] = i
    return []

print(two_sum([2,1,3,2], 4))