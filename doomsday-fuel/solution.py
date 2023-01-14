def solution(m):
    pass

def test(my_solution, inputs, expected = None):
    answer = my_solution(inputs)
    print(f"input: {(inputs)} ... answer: '{answer}', expected: '{expected}'")

if __name__=='__main__':
    print(TREE_STR)
    print()
    test(solution, [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
    test(solution, [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])