#!/usr/bin/env python3

from solution import solution

def run_test(input, expected_output):
    output = solution(input)
    print(input)
    print(expected_output)
    print(output)
    # assert output == expected_output, f"expected: {expected_output} ... got: {output}"

if __name__ == '__main__':
    success, message = [0]*3, [0]*3
    # success[0], message[0] = run_test("code", "100100101010100110100010")
    # success[1], message[1] = run_test("Braille", "000001110000111010100000010100111000111000100010")
    # success[2], message[2] = run_test("The quick brown fox jumps over the lazy dog", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
    # results = [(s,m) for s,m in zip(success, message)]
    # print(*results, sep='\n')
    run_test("code", "100100101010100110100010")
    run_test("Braille", "000001110000111010100000010100111000111000100010")
    run_test("The quick brown fox jumps over the lazy dog", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
