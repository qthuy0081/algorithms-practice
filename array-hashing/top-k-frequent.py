from typing import List, Counter

def top_K_frequent(nums: List[int], k: int) -> List[int]:
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 0
        count_map[num] += 1
    sorted_counter = sorted(count_map.keys(), key=lambda x: count_map[x], reverse=True)
    print(count_map.items())
    return sorted_counter[:k]

def optimized_top_k_frequent(nums: List[int], k: int) -> List[int]:
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 0
        count_map[num] += 1
    bucket = [[] for _ in range(len(nums) +1)]
    for num, count in count_map.items():
        bucket[count].append(num)
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result

if __name__ == '__main__':
    print(top_K_frequent([1,1,1,1,5,5,5,8,9,9,9, 11], 5))
    