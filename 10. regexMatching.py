'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

def isMatch(s, p):
    if not p:
        return not s
    first_match = bool(s) and p[0] in {s[0], "."}

    if len(p) > 1 and p[1] == "*":
        return (isMatch(s, p[2:])) or first_match and isMatch(s[1:], p)
    else:
        return first_match and isMatch(s[1:], p[1:])


print(isMatch("ab", ".*"))