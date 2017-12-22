#! python3
# solution.py
# this code takes a word or phrase and translates it into
# ones and zeros based on braille. Braille as 2 columns of
# 3 rows, which are read top to bottom, left to right to
# make a six digit code where 1 represents a bump and 0
# represents no bump.
# spaces are 000000 and capital letters are preceded by 000001.
# letters are checked to see if they are upper case, then
# the translation is pulled from braille,
# a dictionary that matches the letter to the braille code.
# Letters will be converted to upper before being pulled
# from the dictionary
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

braille = {
    'A':'100000',
    'B':'110000',
    'C':'100100',
    'D':'100110',
    'E':'100010',
    'F':'110100',
    'G':'110110',
    'H':'110010',
    'I':'010100',
    'J':'010110',
    'K':'101000',
    'L':'111000',
    'M':'101100',
    'N':'101110',
    'O':'101010',
    'P':'111100',
    'Q':'111110',
    'R':'111010',
    'S':'011100',
    'T':'011110',
    'U':'101001',
    'V':'111001',
    'W':'010111',
    'X':'101101',
    'Y':'101111',
    'Z':'101011',
    ' ':'000000'
}
capital_letter = '000001'

def answer(plaintext):
    # your code here
    braille_translation = ''
    for letter in plaintext:
        logging.info(letter)
        if letter.isupper():
            braille_translation += capital_letter
        braille_translation += braille[letter.upper()]
        logging.info(braille_translation)
    return braille_translation

# print(answer('code') == '100100101010100110100010')
# print(answer('Braille') == '000001110000111010100000010100111000111000100010')
# print(answer('The quick brown fox jumps over the lazy dog') == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110')
