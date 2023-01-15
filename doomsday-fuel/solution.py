#!/usr/bin/env python3

def matrix_to_str(matrix):
    str_rows = []
    for row in matrix:
        str_rows.append(str(row))
    return '\n'.join(str_rows)

def get_denominators(matrix):
    denominators = []
    for row in matrix:
        d = 0
        for col in row:
            d += col
        denominators.append(d)
    return denominators

def get_probabilities(matrix):
    probabilities = []
    for r_num, row in enumerate(matrix):
        print(r_num, row)
        p_row = []
        denominator = sum(row)
        for col in row:
            p_row.append((col, denominator))
        probabilities.append(p_row)
    return probabilities

    
def solution(m):
    p = get_probabilities(m)
    print("solution: p:\n",matrix_to_str(p))
    state, next = 0, 0
    denominators = []
    visited = set()
    while len(denominators) < len(m):
        if next >= len(m):
            next = 0
            state += 1
            if state >= len(m):
                break
        # print(state, next)
        visited.add( (state, next) )
        numerator, denominator = p[state][next]
        if numerator > 0:
            denominators.append(denominator)
            p[state][next] = (0, denominator)
            if (next, 0) not in visited:
                state = next
                next = 0
        else:
            next += 1
            
    print("denominators:", denominators)

    numerators = [0]*len(m)
    denominator = 1
    for d in denominators:
        if d > 0:
            denominator *= d
    return numerators + [denominator] 

def test(my_solution, inputs, expected = None):
    answer = my_solution(inputs)
    inputs = '\n' + matrix_to_str(inputs)
    print(f"input:{inputs} ... answer: '{answer}', expected: '{expected}'")

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

s0 -> s1 -> s3
s0 -> s1 -> s4
s0 -> s2

s0 -> s1 -> s3 : 2/3 * 3/7 = 6/21
s0 -> s1 -> s4 : 2/3 * 4/7 = 8/21
s0 -> s2 : 1/3 = 7/21

s2: 7, s3: 6, s4: 8




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

s0 -> s5
s0 -> s1 -> s3
s0 -> s1 -> s4

1 + 1 + 4 + 3 + 2 = 11




"""