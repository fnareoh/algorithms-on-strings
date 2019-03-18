def preprocessing_extended_bad_rule(P):
    n = len(P)
    R = {}
    for i in range(n):
        if P[i] not in R:
            R[P[i]] = []
        R[P[i]].append(i)
    return R

def N_preprocessing(P):
    P = P[::-1]
    n = len(P)
    N = [0 for i in range(n)]
    r = l = 0
    for k in range(1,n):
        if r < k :
            n_k = 0
            while k + n_k < n and P[n_k]==P[n_k+k]:
                n_k +=1
            N[k] = n_k
            if n_k > 0:
                l = k
                r = k + n_k - 1
        else:
            k2 = k-l
            if N[k2] < r - k + 1:
                N[k] = N[k2]
            else:
                n_k = r-k+1
                while k + n_k < n and P[n_k]==P[n_k+k]:
                    n_k +=1
                N[k] = n_k
                l = k
                r = k + n_k - 1
    N.reverse()
    return N

def L_and_l_preprocessing(P):
    n = len(P)
    N = N_preprocessing(P)
    L = [0 for i in range(n)]
    l = [0 for i in range(n)]
    for j in range(n-1):
        i = n - N[j]
        if i < n :
            L[i] = j+1
        if N[j] == j+1 :
            l[n-j-1] = j+1
    for i in range(n-2,-1,-1):
        l[i] = max(l[i],l[i+1])
    l[n-1] = n-1
    return L,l

def boyer_moore(P,T):
    res = []
    n = len(P)
    m = len(T)
    R = preprocessing_extended_bad_rule(P)
    L,l = L_and_l_preprocessing(P)

    k = n-1
    while k < m:
        h = k
        i = n-1
        while i >= 0 and T[h]==P[i]:
            i -= 1
            h -= 1
        if i == -1 :
            res.append(k-n+1)
            if len(l) >1 :
                k = k + n - l[1]
            else :
                k = k + 1
        else :
            good_rule = 1
            if i+1 == n:
                pass
            elif L[i+1] > 0 :
                good_rule = n - L[i+1]
            else :
                good_rule = n - l[i+1]

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

            k = k + max(bad_rule,good_rule)

    return res
