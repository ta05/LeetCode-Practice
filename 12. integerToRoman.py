'''
Given an integer, convert it to a roman numeral.
'''



def intToRoman(num):
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

    key_list = list(symbols.keys())
    val_list = list(symbols.values())
    numeral = ""
    while num > 0:
        index = 0
        while index < len(val_list):
            if num >= val_list[index]:
                num -= val_list[index]
                numeral += key_list[index]
                index = 0
            else:
                index += 1
    return numeral

print(intToRoman(100))
print(intToRoman(1998))
