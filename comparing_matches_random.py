import random
import sys
import string
import time

sys.path.insert(0, 'Z_preprocessing')
sys.path.insert(0, 'KMP')

from ref_tryalgo import ref_knuth_morris_pratt
from Z_matching import Z_matching,Z_matching_improved
from KMP import knuth_morris_pratt

n = 1000
m = 100
t = 200

if len(sys.argv) > 1 :
    n = int(sys.argv[1])
if len(sys.argv) > 2 :
    m = int(sys.argv[2])
if len(sys.argv) > 3 :
    m = int(sys.argv[3])

avg_time_KMP_tryalgo = 0
avg_time_KMP = 0
avg_time_Z_matching = 0
avg_time_Z_matching_improved = 0

for i in range(t):
    T = ''.join(random.choices(string.ascii_lowercase, k=n))
    P = ''.join(random.choices(string.ascii_lowercase, k=m))
    i = random.randint(0,len(T))
    T = T[:i] + P + T[i:]
    start = time.time()
    r1 = ref_knuth_morris_pratt(P,T)
    end = time.time()
    avg_time_KMP_tryalgo += end - start
    start = time.time()
    r2 = Z_matching(P,T)
    end = time.time()
    avg_time_Z_matching += end - start
    start = time.time()
    r3 = Z_matching_improved(P,T)
    end = time.time()
    avg_time_Z_matching_improved += end - start
    start = time.time()
    r4 = knuth_morris_pratt(P,T)
    end = time.time()
    avg_time_KMP += end - start
    if r1 != r2 :
        print("PROBLEM : r1 != r2")
        print(P,T,sep="\n")
        print("r1 = ",r1," r2 = ",r2)
    if r1 != r3 :
        print("PROBLEM : r1 != r3")
        print(P,T,sep="\n")
        print("r1 = ",r1," r3 = ",r3)
    if r1 != r4 :
        print("PROBLEM : r1 != r4")
        print(P,T,sep="\n")
        print("r1 = ",r1," r4 = ",r4)

avg_time_KMP_tryalgo = avg_time_KMP_tryalgo/t
avg_time_KMP = avg_time_KMP/t
avg_time_Z_matching = avg_time_Z_matching/t
avg_time_Z_matching_improved = avg_time_Z_matching_improved/t
print("In average, on random strings, Z matching takes ", avg_time_Z_matching/avg_time_KMP_tryalgo," more time than KMP")
print("In average, on random strings, Z matching improved takes ", avg_time_Z_matching_improved/avg_time_KMP_tryalgo," more time than KMP")
print("In average, on random strings, my KMP takes ", avg_time_KMP/avg_time_KMP_tryalgo," more time than KMP")

#print("On english text, Z matching takes ", text_time_Z_matching/text_time_KMP_tryalgo," more time than KMP")
