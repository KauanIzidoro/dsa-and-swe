from binary_gap import solution

def test_solution():
  test_cases = [1041, 9, 529, 20, 15, 32]
  for case in test_cases:
    print(f'{case} - binary = {bin(case)[2:]}, longest gap = {solution(case)}')

test_solution()