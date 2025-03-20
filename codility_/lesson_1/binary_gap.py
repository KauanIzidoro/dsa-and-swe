# Find longest sequence of zeros in binary representation of an integer.

def solution(N: int) -> int:
    binary = bin(N)[2:]
    
    max_gap = 0  
    current_gap = 0  
    counting = False  
    
    for digit in binary:
        if digit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True  
            current_gap = 0  
        elif digit == '0' and counting:
            current_gap += 1
    return max_gap
