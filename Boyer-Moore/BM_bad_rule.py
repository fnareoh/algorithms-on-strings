def boyer_moore(P,T):
    res = []
    n = len(P)
    m = len(T)
    R = {}
    for i in range(len(P)):
        R[P[i]] = i
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
            elif R[T[h]] > i :
                bad_rule = i+1
            else :
                bad_rule = i - R[T[h]]
            k = k + bad_rule
    return res
