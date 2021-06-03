# Sidia 
# Test on Codility

## Dev. Igor Ferreira de Paiva
## June 3, 2021

## TASK 2 ##

def solution(S):
    size = len(S)

    for i in range(size):
        contador = S.count(S[i])
        print(contador)
        if contador == 2:
            #print(S[i])
            return S[i]

#S = "aba"
#solution(S)