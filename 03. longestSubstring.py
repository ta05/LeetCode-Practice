'''
Given a string s, find the length of the longest substring without repeating characters.
'''


# My Original Solution

def lengthOfLongestSubstring(s):
    letter_set = set([])
    curr = ""
    longest = curr

    for letter in s:
        if letter not in letter_set:
            letter_set.add(letter)
            curr = curr + letter
            longest = longest if len(longest) >= len(curr) else curr
        else:
            curr = curr[curr.index(letter) + 1:] + letter
            letter_set = set(list(curr))
    return len(longest)


# Optimized Solution

def lengthOfLongestSubstringOpt(s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)


print(lengthOfLongestSubstring("throwaway"))
print(lengthOfLongestSubstringOpt("superstringed"))