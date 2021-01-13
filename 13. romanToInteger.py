'''
Given a roman numeral, convert it to an integer.
'''

def romanToInt(roman):
    symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    value = 0
    while len(roman) > 0:
        if len(roman) > 1 and symbols.get(roman[0:2]):
            value += symbols.get(roman[0:2])
            roman = roman[2:]
        else:
            value += symbols.get(roman[0])
            roman = roman[1:]
    return value

print(romanToInt("MCMXCVIII"))
print(romanToInt("C"))