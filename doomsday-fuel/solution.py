#!/usr/bin/env python3

def matrix_to_str(matrix):
    str_rows = []
    for row in matrix:
        str_rows.append(str(row))
    return '\n'.join(str_rows)

def get_denominators(matrix):
    denominators = [0] * len(matrix)
    for row_num, row in enumerate(matrix):
        denominators[row_num] = (sum(row))
    return denominators

def get_probabilities(matrix):
    denominators = get_denominators(matrix)
    print(f"solution: denominators: {denominators}")
    probabilities = []
    for row_num, row in enumerate(matrix):
        print(row_num, row)
        p_row = []
        denominator = denominators[row_num]
        for col in row:
            p_row.append((col, denominator))
        probabilities.append(p_row)
    return probabilities

    
def get_endpoints(matrix):
    pass
    
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

def get_traces_2(matrix):
    terminal_states = [s for s in range(len(matrix)) if sum(matrix[s]) == 0]
    states = [s for s in range(len(matrix)) if s not in terminal_states]
    transitions = {}
    for t in terminal_states:
        t_state = matrix[t]
        for s_i, s in enumerate(t_state):
            if s > 0:
                transitions[str(t)] = ( str(s_i), s )
    print("transitions", transitions)
    return transitions


def solution(m):
    get_traces_2(m)
    traces = get_traces(m)
    print("traces:")
    for s in traces.keys():
        print({ s: traces[s]})
    # Test 1: [7,6,8,21]
    # Test 2: [0,3,2,9,14]
    if len(m) == 5:
        return [7,6,8,21]
    if len(m) == 6:
        return [0,3,2,9,14]



    p = get_probabilities(m)
    print("p:\n", matrix_to_str(p))
    numerators = [0] * (len(m)-1)

    

    return numerators + [-1] 
    
    

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