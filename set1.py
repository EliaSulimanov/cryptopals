import codecs
import binascii
import numpy


def hex2base64(hex_text):
    unhex = binascii.unhexlify(hex_text)
    return codecs.encode(unhex, 'base64')


def fixed_xor(feed, xor):
    text1 = bytearray(binascii.unhexlify(feed))
    text2 = bytearray(binascii.unhexlify(xor))
    for i in range(len(text1)):
        text1[i] = text1[i] ^ text2[i]
    return binascii.hexlify(text1)


def single_byte_xor_cipher(ciphered_str):
    unhexed_ciphered_str = bytearray(binascii.unhexlify(ciphered_str))
    latin_letters_byte = bytearray(codecs.encode('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'utf8'))
    score = [0] * len(latin_letters_byte)
    xored_str = bytearray(len(unhexed_ciphered_str))
    for i in range(len(score)):
        for j in range(len(unhexed_ciphered_str)):
            xored_str[j] = unhexed_ciphered_str[j] ^ latin_letters_byte[i]
        for j in range(len(score)):
            score[i] = xored_str.count(latin_letters_byte[14])
    best_score = score.index(max(score))
    for i in range(len(xored_str)):
        xored_str[i] = xored_str[i] ^ latin_letters_byte[best_score]
    return xored_str
