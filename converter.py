def binary_to_decimal(n):
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * (2 ** i)
    return res


def hex_to_decimal(n):
    letters = 'ABCDEF'
    res = 0
    for i in range(len(n)):
        if n[i].isdigit():
            res += int(n[i]) * (16 ** (len(n) - i - 1))
        else:
            res += (letters.find(n[i]) + 10) * 16 ** (len(n) - i - 1)
    return res


def decimal_to_binary(n):
    res = ''
    while n > 0:
        ost = n % 2
        n = n // 2
        res += str(ost)
    return res[::-1]

def decimal_to_octal(n):
    res = ''
    while n > 0:
        ost = n % 8
        n = n // 8
        res += str(ost)
    return res[::-1]

def decimal_to_hex(n):
    letters = 'ABCDEF'
    res = ''
    while n > 0:
        ost = n % 16
        n = n // 16
        if ost >= 10:
            index = ost - 10
            res += letters[index]
        else:
            res += str(ost)
    return res[::-1]



n = int(input())
print(decimal_to_hex(n))