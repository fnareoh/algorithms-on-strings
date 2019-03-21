import math
import cmath

def FFT_rec(A, invert):
    n = len(A)
    if n == 1:
        return
    A0,A1 = [A[i] for i in range(0,n,2)],[A[i] for i in range(1,n,2)]

    FFT_rec(A0,invert)
    FFT_rec(A1,invert)

    wn = cmath.exp( 2j*math.pi* (-1 if invert else 1) / n)
    w = 1
    for i in range(n//2):
        A[i] = A0[i] + w*A1[i]
        A[i + n//2] = A0[i] - w*A1[i]
        if invert:
            A[i] /= 2
            A[i + n//2] /= 2
        w *= wn

def rev(k, n):
    if k % 2 == 0:
        return k//2
    else :
        return n//2 + (k-1)//2

def FFT_it(a, invert):
    n = len(a)
    lg_n = int(math.log(n,2))
    A = [0]*n
    for k in range(n):
        A[rev(k,n)] = a[k]
    for s in range(1,lg_n+1):
        m = pow(2,s)
        wm = cmath.exp( 2j*math.pi* (-1 if invert else 1) / m)
        for k in range(0,n,m):
            w = 1
            for i in range(m//2):
                t = w*A[k+i+m//2]
                u = A[k+i]
                A[k + i] = u + t
                A[k + i + m//2] = u - t
                w *= wm
    if invert:
        for i in range(n):
            A[i] /= n
    return A

def multiply(A,B):
    n = 1
    while n < len(A) + len(B) :
        n *= 2
    FA = A + [0]*(n-len(A))
    FB = B + [0]*(n-len(B))
    FA2 = A + [0]*(n-len(A))
    FB2 = B + [0]*(n-len(B))


    FA = FFT_it(FA, False)
    FB = FFT_it(FB, False)
    for i in range(n):
        FA[i] *= FB[i]
    FA = FFT_it(FA, True)


    result = [round(FA[i].real) for i in range(n)]
    return result

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print("result:", multiply(A,B))

main()
