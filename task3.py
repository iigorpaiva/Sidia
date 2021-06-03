# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, L):
    print(sum(A))
    if len(A) < (K + L):
        return - 1
    
    if len(A) == (K+L):
        return sum(A)
        


A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2

# INCOMPLETE

solution(A, K, L)