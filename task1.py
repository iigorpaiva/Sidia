def solution(S):

    size = len(S)
    if size == 0:
        pass
    for i in range(0, size // 2):
        #print(i)
        #print("i: ", i, " and after half: ", (size - i - 1))
        print("i: ", S[i], " and after half: ", S[(size - i - 1)])
        if S[i] != S[size - i - 1]:
            if S[i] == "?" and S[size - i - 1] != "?":
                S = S[0:i] + S[size - i - 1] + S[i+1:]
            elif S[i] != "?" and S[size - i - 1] == "?":
                S = S[0:(size - i - 1)] + S[0:i] + S[(size - i):] # acho que o erro tá aqui
                #S = S.replace(S[size - i - 1], S[i], 1)
            else:
                print("NO")
                return "NO"
        else:
            if S[size - i - 1] == "?" and S[i] == "?":
                S = S[0:i] + "z" + S[i+1:]
                S = S[0:(size - i - 1)] + "z" + S[(size - i)+1:]
    print(S)
    return S

solution("?ab??a")
#solution("bab??a")
#solution("?a?")