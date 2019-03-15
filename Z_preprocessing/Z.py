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
				z_k = Z[k2]
				while k + z_k < n and S[z_k] == S[k + z_k]:
					z_k += 1
				Z[k] = z_k
				l = k
				r = k + z_k - 1
	return Z



P = input()
Z = Z_algo(P)
n = len(Z)
for i in range(n): print(i,end=" ")
print()
for i in range(n): print(Z[i],end=" ")
print()
