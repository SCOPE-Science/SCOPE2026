"""Literal position-subsequence enumeration versus the cyclic Moore machine."""
from itertools import product,combinations
from math import comb

def parity_literal(word, k):
    p=tuple(j%2 for j in range(k))
    return sum(all(word[i]==p[j] for j,i in enumerate(positions))
               for positions in combinations(range(len(word)),k))%2

def output_cyclic(word,k):
    L=1<<k.bit_length()
    t=0
    for c in word:
        t=(-t-1 if c==0 else -t)%L
    u=(t+k//2)%L
    return int((u&k)==k)

def main():
    tests=0
    for n in range(0,13):
        for w in product((0,1),repeat=n):
            for k in range(1,13):
                a=parity_literal(w,k)
                b=output_cyclic(w,k)
                assert a==b,(w,k,a,b)
                tests+=1
    print('literal_vs_cyclic PASS cases='+str(tests)+' words='+str(sum(1<<n for n in range(13))))
if __name__=='__main__':main()
