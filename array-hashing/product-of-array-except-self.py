from typing import List
import math
def product_except_self(arr: List[int]) -> List[int]:
    result = [1] * len(arr)
    left_product, right_product = 1, 1
    for i in range(len(arr)):
        result[i] *= left_product
        left_product *= arr[i]
    for i in range(len(arr) - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    return result

print(product_except_self([1,2,4 ,6]))