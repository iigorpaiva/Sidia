# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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