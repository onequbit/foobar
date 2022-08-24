#!/usr/bin/env python

# Level 1 - Problem 1

def solution(x):
    import string
    key = {}
    lowercase_letters = [l for l in string.ascii_lowercase]
    lowercase_reverse = lowercase_letters[::-1]
    for i in range(len(lowercase_letters)):
        key[lowercase_reverse[i]] = lowercase_letters[i]
    plaintext = [c for c in x]
    for index,letter in enumerate(x):
        if letter in lowercase_letters:
            plaintext[index] = key[letter]
    return ''.join(plaintext)

def test(s):
    answer = solution(s)
    print(answer)


test("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
test("wrw blf hvv ozhg mrtsg'h vkrhlwv?")

