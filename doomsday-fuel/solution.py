#!/usr/bin/env python3
import json
from functools import reduce
import operator
from fractions import Fraction

def matrix_to_str(matrix):
    str_rows = []
    for row in matrix:
        row_str = ""
        for _, col in enumerate(row):
            row_str += f"{str(col)} "
        str_rows.append(row_str)
    return '\n' + '\n'.join(str_rows)



def to_fractions(matrix):
    m2 = []
    denominators = []
    for row_num, row in enumerate(matrix):
        d = sum(matrix[row_num])
        m2_row = []
        for col_num, col in enumerate(row):
            numerator = col
            f = f"{numerator}/{d}" if numerator > 0 else 0
            m2_row.append(f)
        m2.append(m2_row)
        denominator = sum([Fraction(m).numerator for m in m2_row if m != 0])
        denominators.append(denominator)
    return m2, denominators

def solution(m):
    m2, denominators = to_fractions(m)    
    denominator = reduce(operator.mul, [d for d in denominators if d > 0])
    output_rows = []
    for i, d in enumerate(denominators):
        if d == 0:
            output_rows.append(i)
    input_counts = [sum(row) for row in m]
    input_count = reduce(operator.mul, [i for i in input_counts if i > 0])
    
    column = 0
    row = 0
    outputs = [0] * len(m)
    while column < len(m) and row < len(m):
        cell = m2[row][column]
        
        if Fraction(cell) > 0:
            for i, t in enumerate(m2[column]):
                if Fraction(t) > 0:
                    a,b = Fraction(t).as_integer_ratio()
                    c,d = Fraction(cell).as_integer_ratio() 
                    new_frac = Fraction( a*c, b*d )
                    m2[column][i] = str(new_frac)
                    outputs[i] = input_count * Fraction(t)
        if column in output_rows and Fraction(cell) > 0:
            outputs[column] = Fraction(cell) * input_count
            
        column += 1
        if column == len(m):
            column = 0
            row += 1
    
    probabilities = [int(o) for i, o in enumerate(outputs) if i in output_rows]
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


s0->s1: 2, s0->s2: 3
s1->s3: 3, s1->s4: 4

s0->s1->s3: 2/3 * 3/7 = 6/21 
s0->s1->s4: 2/3 * 4/7 = 8/21
s0->s2: 1/3


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

s0->s1: 1/2
s0->s5: 1/2 ... * 18 = 9
s1->s0:? 1/2 * 4/9 = 4/18 = 2/9 ... * 18 = 4 
s1->s3: 1/2 * 3/9 = 3/18 ... * 18 = 3
s1->s4: 1/2 * 2/9 = 2/18 ... * 18 = 2

"""