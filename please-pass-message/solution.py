from itertools import permutations 

def solution(l):
    digits = [str(d) for d in l]
    numbers = []
    for r in range(1,len(l)+1):
        perms = [''.join(p) for p in permutations(digits, r)]
        numbers += [int(p) for p in perms if int(p) % 3 == 0]
    if len(numbers) == 0:
        return 0
    else:
        return max(numbers)
    
    
def test(my_solution, input, expected = None):
    answer = my_solution(input)
    print(f"input: {input} ... answer: {answer}")
    # assert answer == expected, f"answer: {answer}, expected:{expected}"

"""
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
"""
if __name__=='__main__':
   test(solution, [3,1,4,1], expected=4311)
   test(solution, [3, 1, 4, 1, 5, 9], expected=954311)
   test(solution, [1,2,3])
   test(solution, [1,2,4,3])
   test(solution, [5,8,9])
   test(solution, [7,8,9])