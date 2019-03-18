def preprocessing_extended_bad_rule(P):
    n = len(P)
    R = {}
    for i in range(n):
        if P[i] not in R:
            R[P[i]] = []
        R[P[i]].append(i)
    return R


def boyer_moore(P,T):
    res = []
    n = len(P)
    m = len(T)
    R = preprocessing_extended_bad_rule(P)

    k = n-1
    while k < m:
        h = k
        i = n-1
        while i >= 0 and T[h]==P[i]:
            i -= 1
            h -= 1
        if i == -1 :
            res.append(k-n+1)
            k = k + 1
        else :
            bad_rule = 1
            if T[h] not in R:
                bad_rule = i+1
            elif R[T[h]][0] > i :
                bad_rule = i+1
            else :
                a = 0
                b = len(R[T[h]])-1
                while a != b :
                    mil = (a+b)//2
                    if R[T[h]][mil+1] < i :
                        a = mil+1
                    else :
                        b = mil
                bad_rule = i-R[T[h]][a]

            k = k + bad_rule

    return res
