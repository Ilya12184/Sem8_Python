msg = input('msg = ')
shift = int(input('shift = '))

def encrypt_caesar(msg, shift=3):
    symbol_big = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    symbol_litle = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for i in msg:
        if i in symbol_big:
            mesto = symbol_big.find(i)
            new_mesto = mesto + shift
            result += symbol_big[new_mesto]
        elif i in symbol_litle:
            mesto = symbol_litle.find(i)
            new_mesto = mesto + shift
            result += symbol_litle[new_mesto]
        else:
            result += i
    return result

encrypted = encrypt_caesar(msg, shift)


def decrypt_caesar(encrypted, shift=3):
    return encrypt_caesar(encrypted, -1 * shift)

decrypted = decrypt_caesar(encrypted, shift)


print(encrypted)
print(decrypted)