from typing import List

s_array = ["act","pots","tops","cat","stop","hat"]

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for s in strs:
        sorted_str = "".join(sorted(s))
        if sorted_str not in anagram_groups:
            anagram_groups[sorted_str] = []
        anagram_groups[sorted_str].append(s)
    return list(anagram_groups.values())

def optimized_group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for s in strs:
        alpha_count = [0] * 26
        for c in s:
            alpha_count[ord(c) - ord('a')] += 1
        key = ",".join(str(x) for x in alpha_count)
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups.get(key).append(s)
    return list(anagram_groups.values())

print(group_anagrams(s_array))
print(optimized_group_anagrams(s_array))
