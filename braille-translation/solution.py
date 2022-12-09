#!/usr/bin/env python3
import string
# Input:
# Solution.solution("The quick brown fox jumps over the lazy dog")
# Output:
#     000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

"""
100100101010100110100010
100100, 101010, 100110, 100010

000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
000001,011110,110010,100010,000000,111110,101001,010100,100100,101000,000000,110000,111010,101010,010111,101110,000000,110100,101010,101101,000000,010110,101001,101100,111100,011100,000000,101010,111001,100010,111010,000000,011110,110010,100010,000000,111000,100000,101011,101111,000000,100110,101010,110110
     ^      T      h      e      _      q      u      i      c      k      _      b      r      o      w      n      _      f      o      x      _      j      u      m      p      s      _      o      v      e      r      _      t      h      e      _      l      a      z      y      _      d      o      g


"""




def make_decoder():
    alphabet_message = "The quick brown fox jumps over the lazy dog"
    braille_message = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    message_copy = ''
    for char in alphabet_message:
        if char in string.ascii_uppercase:
            message_copy += '~'
        message_copy += char             
    braille_chars = {}
    for index, char in enumerate(message_copy):
        braille_dots = ''
        for step in range(6):
            char_position = (index * 6) + step
            character = braille_message[char_position]
            braille_dots += character
        braille_chars[str(char).lower()] = braille_dots
    return braille_chars


def solution(s):
    # Your code here
    decoder = make_decoder()
    dots = ''
    for char in s:
        if char in string.ascii_uppercase:
            dots += decoder['~']
        dots += decoder[str(char).lower()]
    return dots

    
if __name__ == "__main__":
    
    pass