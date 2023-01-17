#!/usr/bin/env python3
import json

from fractions import Fraction

def matrix_to_str(matrix):
    str_rows = []
    for row in matrix:
        str_rows.append(str(row))
    return '\n' + '\n'.join(str_rows)

# def get_denominators(matrix):
#     denominators = [0] * len(matrix)
#     for row_num, row in enumerate(matrix):
#         denominators[row_num] = (sum(row))
#     return denominators

# def get_probabilities(matrix):
#     denominators = get_denominators(matrix)
#     print(f"solution: denominators: {denominators}")
#     probabilities = []
#     for row_num, row in enumerate(matrix):
#         print(row_num, row)
#         p_row = []
#         denominator = denominators[row_num]
#         for col in row:
#             p_row.append((col, denominator))
#         probabilities.append(p_row)
#     return probabilities

    
def get_traces(matrix):
    traces = {}
    for state, row in enumerate(matrix):
        state_id = f"s{state}"
        # traces[state_id] = row
        denominator = sum(row)
        if denominator > 0:
            s_next = set()
            for s_index, s in enumerate(row):
                if s > 0:
                    s_id = f"s{s_index}"
                    s_next.add((s_id, s, denominator))
            traces[state_id] = s_next
    return traces

def propagate_probabilities(matrix):
    print("propagate_probabilities")
    for row_num, row in enumerate(matrix):
        for i, r in enumerate(row):
            p,d = r
            if p > 0:
                p1, d1 = matrix[i][row_num]
                print(f"p1: {p1}, d1: {d1}... ", end='')
                p1 *= p / d

                #  TO DO: Propagate this new probability into denominators
                
                matrix[i][row_num] = (p1, d1)
                print(f"matrix[{i}][{row_num}]: {matrix[i][row_num]}, ", end='')
        print()
    return matrix

def solution(m):
    # print(f"inputs:{matrix_to_str(m)}")
    m2 = [[Fraction(number) for number in row] for row in m]
    # print(f"inputs:{matrix_to_str(m2)}")
    result_rows = []
    denominators = []
    for row_num, row in enumerate(m2):
        d = sum([r.numerator for r in row])
        # print(f"iteration:{row_num} --> m:{matrix_to_str(m2)}") 
        for i, p in enumerate(row):
            if p > 0:
                c = Fraction(p,d)
                n = m2[i][row_num].numerator * c
                m2[i][row_num] = Fraction(n, 1)
        d = sum([r.numerator for r in row])
        if d > 0:
            denominators.append(d)
        else:
            result_rows.append(row_num)
        print(f"status m:{matrix_to_str(m)}")
        print(f"status m2:{matrix_to_str(m2)}")
    print(f"denominators:{denominators}")
    print(f"result_rows:{result_rows}")

    denominator = 1
    for d in denominators:
        denominator *= d
    probabilities = [0] * len(m)

    m2 = m.copy()
    
    for row_num, row in enumerate(m2):
        for i, r in enumerate(row):
            if r > 0:
                

                # m2[i][row_num] *= m[row_num][i]
    print(f"new m:{matrix_to_str(m)}")
    # if len(m) == 5:
    #     return [7,6,8,21]
    # if len(m) == 6:
    #     return [0,3,2,9,14]
    print(get_traces(m))
    
    return probabilities + [denominator]
    
    

def test(my_solution, inputs, expected = None):
    answer = my_solution(inputs)
    inputs = '\n' + matrix_to_str(inputs)
    print(f"... answer: '{answer}', expected: '{expected}'")

if __name__=='__main__':
    print()
    test(solution, [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]], expected=[7, 6, 8, 21])
    test(solution, [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [0, 3, 2, 9, 14])

"""
test(solution, 
[
    [0, 2, 1, 0, 0], 
    [0, 0, 0, 3, 4], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
], 
expected=[7, 6, 8, 21])



s0 -> s2: 1/3 -> 7/21
s0 -> s1 -> s3: 2/3 * 3/7 -> 6/21
s0 -> s1 -> s4: 2/3 * 4/7 -> 8/21


test(solution, 
[
    [0, 1, 0, 0, 0, 1], 
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
], 
expected=[0, 3, 2, 9, 14])

s0 -> s1: 50%
s0 -> s5: 50%
s1 -> s0 -> ((1/2)*4)/9
s2 <- 0
s3 <- s1 <- s0: 3/9 * (1/2 + 4/9)
s4 <- s1 <- s0: 2/9 * (1/2 + 4/9)
s5 <- s0: 1/2


s0 <- s1(4/9)
s1 <- s0(1/2)
s2 <- 0
s3 <- s1(3/9) * s0(1/2)
s4 <- s1(2/9) * s0(1/2)
s5 <- s0(1/2) + s1(4/9)




s0 -> s5
s0 -> s1 -> s3
s0 -> s1 -> s4

1 + 1 + 4 + 3 + 2 = 11




"""