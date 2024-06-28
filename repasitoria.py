def arabic_to_roman(num):
    if num <= 0:
        raise ValueError("Number must be greater than 0")

    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    roman_result = ""
    for value, numeral in roman_numerals:
        while num >= value:
            roman_result += numeral
            num -= value

    return roman_result

# Test cases
print(arabic_to_roman(10))  # Expected output: XV
print(arabic_to_roman(72))  # Expected output: LXXII
print(arabic_to_roman(9))   # Expected output: IX