'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

def convert(s: str, numRows: int):
    if numRows == 1:
        return s
    ret = ""
    n = len(s)
    cycle_len = 2 * numRows - 2

    for i in range(0, numRows):
        j = 0
        while j + i < n:
            ret += s[j + i]
            if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                ret += s[j + cycle_len - i]
            j += cycle_len
            
    return ret

print(convert("PAYPALISHIRING", 6))