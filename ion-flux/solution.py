from math import log # log( number, base )

TREE_STR = """
                                                    63
                    31                                                              62
        15                          30                              46                              61
   7        14              22              29              38              45              53              60
 3   6   10     13      18      21      25      28      34      37      41      44      49      52      56      59
1 2 4 5 8  9  11  12  16  17  19  20  23  24  26  27  32  33  35  36  39  40  42  43  47  48  50  51  54  55  57  58
"""

"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 

1 1 2 1 1 2 3 1 1  2  1  1  2  3  4  1  1  2  1  1  2  3  1  1  2  1  1  2  3  4  5  1  1  2  1  1  2  3  1  1  2  1  1  2  3  4  1  1  2  1  1  2  3  1  1  2  1  1  2  3  4  5  6
"""

"""
parents:
63     62      61      60      59 ...
63-32  62-16   61-8    60-4    59-2 ...
31-16  30-8    29-4    28-2 ...
15-8   22-4    25-2    ...
7-4    10-2    ...

2^6-1         2^6-2         2^6-3       2^6-4       2^6-5
2^6-1 - 2^5   2^6-2 - 2^4   2^6 - 2^3   2^6 - 2^2   2^6 - 2^1
63-32         62-16   61-8    60-4    59-2 ...
31-16         30-8    29-4    28-2 ...
15-8          22-4    25-2    ...
7-4           10-2    ...
"""


SUBTREE = {
    1 : 2,
    2 : 1,
    4 : 2,
    5 : 1,
    3 : 4,
    6 : 1
}

def tree_parent(h, node):
    print(f"tree_parent( {h}, {node} )")
    tree = [i for i in range(1,(2**h))]
    if node >= tree[-1]:
        return -1
    two_powers = [2**p for p in range(0,h+1)]
    left_edges = [e-1 for e in two_powers]
    if node in left_edges and (node * 2) + 1 in left_edges:
        return (node * 2) + 1
    right_edges = [t for t in range(2**h,(2**h)-h,-1)]
    if node in right_edges and node + 1 in right_edges:
        return node + 1
    if node in SUBTREE.keys():
        return node + SUBTREE[node]
    subtree_height = int(log(node, 2))
    subtree_node = node - ((2**subtree_height)-1)
    print(f"node: {node}, subtree_height: {subtree_height}, subtree_node: {subtree_node}")
    if subtree_node in SUBTREE.keys():
        return node + SUBTREE[subtree_node]
    if subtree_node in left_edges and (subtree_node * 2) + 1 in left_edges:
        return (subtree_node * 2) + 1
    if subtree_node in right_edges and subtree_node + 1 in right_edges:
        return subtree_node + 1
    parent = tree_parent(subtree_height, subtree_node)
    print(f"node: {node}, subtree_height: {subtree_height}, subtree_node: {subtree_node}, parent: {parent}")
    return node + parent

def solution(h, q):    
    p = []
    for value in q:
        p.append(tree_parent(h, value))
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
    print(TREE_STR)
    print()
    test(solution, 3, [7, 3, 5, 1], expected=[-1,7,6,3])
    test(solution, 5, [19, 14, 28], expected=[21,15,29])
#    test(solution, 4, [1,2,3])
#    test(solution, 6, [1,2,4,3])
#    test(solution, 7, [5,8,9])
#    test(solution, 8, [7,8,9])
    # for i in range(3,64):
    #     l, u = nearest_two_powers(i)
    #     # d = (2**u) - i
    #     d = ((2**u)-1)-i   # ( i-((2**l)-1) ) # , ((2**u)-1)-i )
    #     print(f"{i}: 2^{l}..2^{u}, . . . d :: {d}")
        # for j in range(6):
        #     tree_parent(i,j)
