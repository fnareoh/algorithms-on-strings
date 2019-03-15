import random
import sys
import string
import time

sys.path.insert(0, 'Z_preprocessing')
sys.path.insert(0, 'Boyer-Moore')
sys.path.insert(0, 'KMP')

from ref_tryalgo import ref_knuth_morris_pratt
from Z_matching import Z_matching,Z_matching_improved
from boyer_moore import boyer_moore
from KMP import knuth_morris_pratt

T = ""
fobj = open("english.200MB.txt", encoding='utf-8', errors='ignore')
for line in fobj:
    T += line.rstrip()
fobj.close()

most_common_words = []
fobj = open("most_common_words_english.txt", encoding='utf-8', errors='ignore')
for line in fobj:
    word = line.rstrip()
    if word != "": most_common_words.append(word)
fobj.close()

n = len(T)

if len(sys.argv) > 1 :
    n = int(sys.argv[1])

avg_time_KMP_tryalgo = 0
avg_time_KMP = 0
avg_time_Z_matching = 0
avg_time_Z_matching_improved = 0
avg_time_boyer_moore = 0

for P in most_common_words:
    start_T = random.randint(0,len(T)-n)
    start = time.time()
    r1 = ref_knuth_morris_pratt(P,T[start_T:start_T+n])
    end = time.time()
    avg_time_KMP_tryalgo += end - start
    start = time.time()
    r2 = Z_matching(P,T[start_T:start_T+n])
    end = time.time()
    avg_time_Z_matching += end - start
    start = time.time()
    r3 = Z_matching_improved(P,T[start_T:start_T+n])
    end = time.time()
    avg_time_Z_matching_improved += end - start
    # start = time.time()
    # r4 = boyer_moore(P,T[start_T:start_T+n])
    # end = time.time()
    # avg_time_boyer_moore += end - start
    start = time.time()
    r5 = knuth_morris_pratt(P,T[start_T:start_T+n])
    end = time.time()
    avg_time_KMP += end - start
    if r1 != r2 :
        print("PROBLEM : r1 != r2")
        print(P,T[start_T:start_T+n],sep="\n")
        print("r1 = ",r1," r2 = ",r2)
    if r1 != r3 :
        print("PROBLEM : r1 != r3")
        print(P,T[start_T:start_T+n],sep="\n")
        print("r1 = ",r1," r3 = ",r3)
    # if r1 != r4 :
    #     print("PROBLEM : r1 != r4")
    #     print(P,T[start_T:start_T+n],sep="\n")
    #     print("r1 = ",r1," r4 = ",r4)
    if r1 != r5 :
        print("PROBLEM : (ref) r1 != r5 (KMP)")
        print("r1 \ r5 : ", [val for val in r1 if val not in r5], " r5 \ r1: " ,[val for val in r5 if val not in r1])
        #print(P,T,sep="\n")
        #print("r1 = ",r1," r5 = ",r5)

t = len(most_common_words)
avg_time_KMP_tryalgo = avg_time_KMP_tryalgo/t
avg_time_KMP = avg_time_KMP/t
avg_time_Z_matching = avg_time_Z_matching/t
avg_time_Z_matching_improved = avg_time_Z_matching_improved/t
avg_time_boyer_moore = avg_time_boyer_moore/t
print("In average, on an english text, Z matching takes ", avg_time_Z_matching/avg_time_KMP_tryalgo," more time than KMP")
print("In average, on an english text, Z matching improved takes ", avg_time_Z_matching_improved/avg_time_KMP_tryalgo," more time than KMP")
print("In average, on an english text, Boyer Moore takes ", avg_time_boyer_moore/avg_time_KMP_tryalgo," more time than KMP")
print("In average, on an english text, my KMP takes ", avg_time_KMP/avg_time_KMP_tryalgo," more time than KMP")

#print("On english text, Z matching takes ", text_time_Z_matching/text_time_KMP_tryalgo," more time than KMP")
