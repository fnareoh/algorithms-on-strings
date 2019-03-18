def knuth_morris_pratt(P,T):
    n = len(P)
    m = len(T)
    R = [0 for i in range(n)]
    j = R[0] = -1

    for i in range(1,n):
        while j >= 0 and (P[i-1] != P[j] or (j+1 < n and P[i] == P[j+1])) :
            j = R[j]
        j+=1
        R[i] = j

    j = 0
    res = []
    for i in range(m):
        while j>=0 and T[i]!=P[j]:
            j = R[j]
        j+=1
        if (j==n):
            res.append(i-n+1)
            if n == 1:
                j = 0
            else:
                j = R[n-1]
    return res
