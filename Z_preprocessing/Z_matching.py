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

def Z_matching_improved(P,T):
	Z = Z_algo(P)
	r = l = -1
	n = len(P)
	m = len(T)
	res = []
	for k in range(len(T)):
		if k > r :
			z_k = 0
			while z_k < n and k + z_k < m and P[z_k] == T[k + z_k]:
				z_k += 1
			if z_k >= len(P):
				res.append(k)
			if z_k > 0 :
				l = k
				r = k + z_k - 1
		else:
			k2 = k - l
			if Z[k2] < r-k+1:
				pass
			else :
				z_k = r-k+1
				while z_k < n and k + z_k < m and P[z_k] == T[k + z_k]:
					z_k += 1
				if z_k >= n :
					res.append(k)
				l = k
				r = k + z_k - 1
	return res
