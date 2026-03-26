#Given two string `s` and `t`, return true if the two string are anagrams of each other, otherwise return false.

t = '121212'
s = '2121211'

def is_anagram(s: str, t: str):
    if len(s) != len(t): return  False
    my_dict = {}
    for c in s:
        my_dict[c] = my_dict.get(c, 0) + 1

    for c in t:
        my_dict[c] = my_dict.get(c, 0) - 1

    for count in my_dict.values():
        if count != 0:
            return  False
    return True

print(is_anagram(t,s))