

def is_palindrome(s: str) -> bool:
    #used to hold only alphabet and number
    temp_str = ''

    for c in s:
        if c.isalnum():
            temp_str += c.lower()
    return temp_str == temp_str[::-1]

def is_palindrome_optimized(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l +=1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

s_input = "Was it a car or a cat I saw?"
s01 = "tab a cat"

print(is_palindrome(s_input))
print(is_palindrome_optimized(s01))