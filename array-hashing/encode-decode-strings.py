from typing import List



def encode(strs: List[str]) -> str:
    result = ''
    for s in strs:
        result += str(len(s)) + '#' + s
    return result
def decode(s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        word_length = int(s[i:j])
        word_start = j + 1
        word_end = word_length + word_start
        result.append(s[word_start:word_end])
        i = word_end
    return result




input_data = ['hello, world', 'i', 'love', '3#python3']
encoded_s = encode(input_data)
print(encoded_s)
print(decode(encoded_s))