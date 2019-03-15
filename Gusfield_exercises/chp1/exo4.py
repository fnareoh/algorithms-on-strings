import math

def Z_algo(S):
	n = len(S)
	Z = [0 for i in range(n)]
	Z[0] = n
	r = l = 0
	for k in range(1,n):
		if k > r :
			z_k = 0
			while k + z_k < n and S[z_k] == S[k + z_k]:
				z_k += 1
			Z[k] = z_k
			if z_k > 0 :
				l = k
				r = k + z_k - 1
		else:
			k2 = k - l
			if Z[k2] < r-k+1:
				Z[k] = Z[k2]
			else :
				z_k = r-k+1
				while k + z_k < n and S[z_k] == S[k + z_k]:
					z_k += 1
				Z[k] = z_k
				l = k
				r = k + z_k - 1
	return Z

def Z_matching(P,T):
	Z = Z_algo(P+'#'+T)
	res = []
	for i in range(len(P)+1,len(P)+len(T)+1):
		if (Z[i] >= len(P)):
			res.append(i - len(P) - 1)
	return res


def find_maximal_tandem(beta, S):
    n = len(S)
    p = len(beta)
    power_beta = math.ceil(n/p)
    Z = Z_algo(beta*power_beta+"#"+S)

    maximals = []
    p_max = -1
    r_max = -1
    for i in range(p*power_beta+1,len(Z)):
        if Z[i]//p > 1:
            end_i = Z[i] - (Z[i] % p)
            if (i + end_i  > r_max) :
                maximals.append((i- (p*power_beta+1),Z[i]//p))
                p_max = i
                r_max = i + end_i
            elif  i - p_max < p:
                maximals.append((i- (p*power_beta+1),Z[i]//p))
    return maximals

beta = "abab"
S = "abababababab"
print(find_maximal_tandem(beta,S))
