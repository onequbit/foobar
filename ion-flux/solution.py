from math import log # log( number, base )

def nearest_two_power(n):
    lower = int(log(n, 2))
    upper = lower+1
    

def tree_parent(h, node):
    print("tree h:", h)
    tree = [i for i in range(1,(2**h))]
    if node == tree[-1]:
        return -1
    if node*2 > tree[-1]:
        return -1
    two_powers = [2**t for t in range(1,h+1)]
    left_edges = [e-1 for e in two_powers]
    if node in left_edges and (node * 2) + 1 in left_edges:
        return (node * 2) + 1
    right_edges = [tree[-1] - i for i in range(0,h)]
    if node in right_edges and node + 1 in right_edges:
        return node + 1
    print("two:", two_powers)
    print("left:", left_edges)
    print("right:", right_edges)
    return -1

def solution(h, q):    
    # if (h,q) == (3, [7, 3, 5, 1]):
    #    return [-1,7,6,3]
    # if (h,q) == (5, [19, 14, 28]):
    #    return [21,15,29]
    p = [-1] * len(q)
    for i, value in enumerate(q):
        p[i] = tree_parent(h, value)
        
    return p


def test(my_solution, input_h, input_q, expected = None):
    answer = my_solution(input_h, input_q)
    print(f"input: {(input_h, input_q)} ... answer: '{answer}', expected: '{expected}'")


"""
Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3

Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29
"""
if __name__=='__main__':
#    test(solution, 3, [7, 3, 5, 1], expected=[-1,7,6,3])
#    test(solution, 5, [19, 14, 28], expected=[21,15,29])
#    test(solution, 4, [1,2,3])
#    test(solution, 6, [1,2,4,3])
#    test(solution, 7, [5,8,9])
#    test(solution, 8, [7,8,9])
    for i in range(3,6):
        for j in range(6):
            tree_parent(i,j)
