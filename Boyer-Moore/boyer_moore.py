def preprocessing_extended_bad_rule(P):
    n = len(P)
    ##print("len(P): ", len(P))
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
    # print("N: ", N)
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

def dicho(i,a,b,R):
    if a == b :
        return i-R[a]
    m = (a+b)//2
    if R[m+1] < i :
        return dicho(i,m+1,b,R)
    else :
        return dicho(i,a,m,R)

def bad_rule(i, T_h, R,n):
    if T_h not in R:
        return n - i
    if R[T_h][0] > i :
        return n - i
    return dicho(i,0,len(R[T_h])-1,R[T_h])

def good_rule(i,L,l):
    n = len(L)
    if i == n:
        return 1
    if L[i] > 0 :
        return n - L[i]
    else :
        return n - l[i]


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
            # print("h: ", h, "k: ", k, "i: ",i," T[h]: ", T[h])
            # print("bad rule: ", bad_rule(i,T[h],R,n), "good rule: ", good_rule(i+1,L,l))
            k = k + max(bad_rule(i,T[h],R,n),good_rule(i+1,L,l))
        # print("R: ", R)
        # print("L: ", L)
        # print("l: ", l)
    return res


# P = input()
# T = input()
# print(boyer_moore(P,T))
