def solution(S):

    size = len(S) - 1
    if size == 0:
        pass
    for i in range(0, (((size) + 1) // 2)):
        #print("i: ", S[i], " and after half: ", S[(size - i )])
        if S[i] != S[size - i]:
            if S[i] == "?" and S[size - i] != "?":
                print("primeiro")
                S = S[0:i] + S[size - i] + S[i+1:]
            elif S[i] != "?" and S[size - i] == "?":
                print("segundo: ", S[size])
                S = S[0:(size - i)] + S[i] + S[(size - i) +1:]
                #S = S.replace(S[size - i], S[i], 1)
            else:
                #print("NO")
                return "NO"
        else:
            if S[size - i] == "?" and S[i] == "?":
                S = S[0:i] + "z" + S[i+1:]
                S = S[0:(size - i)] + "z" + S[(size - i)+1:]
    #print(S)
    return S

#solution("?ab??a")
#solution("bab??a")
#solution("?a?")