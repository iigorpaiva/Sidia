# Sidia 
# Test on Codility

## Dev. Igor Ferreira de Paiva
## June 3, 2021

## TASK 3 ##

def solution(A, K, L):

    if len(A) < (K + L):
        return - 1
    elif len(A) == (K+L):
        return sum(A)
    else:
        for i in range(K):
            sum(A[K])
            
A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2

# INCOMPLETE

solution(A, K, L)