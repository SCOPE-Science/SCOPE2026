#!/usr/bin/env python3
"""Independent all-character modular certificate for three by three Fourier minors on Z_30."""
from collections import Counter
from itertools import combinations
from math import gcd

N, P, PRIMITIVE_ROOT = 30, 1201, 11
assert (P - 1) % N == 0
assert len({pow(PRIMITIVE_ROOT, i, P) for i in range(1, P)}) == P-1
units = [k for k in range(1,N) if gcd(k,N)==1]
assert len(units)==8
powers = [[pow(pow(PRIMITIVE_ROOT, (P-1)*k//N,P),e,P) for e in range(N)] for k in units]
for row in powers:
    assert len(set(row)) == N

T = list(combinations(range(1,N),2))
cnt=Counter()
for a,b in T:
    for c,d in T:
        ex = [(a*c+b*d)%N,(a*d+b*c)%N,(a*c)%N,(b*d)%N,(a*d)%N,(b*c)%N]
        sg = [1,-1,-1,-1,1,1]
        is_zero=all(sum(s*row[e] for s,e in zip(sg,ex))%P==0 for row in powers)
        rank = (1 if a*c%N==a*d%N==b*c%N==b*d%N==0 else 2) if is_zero else 3
        cnt[rank]+=1
assert cnt == Counter({1:180,2:15192,3:149464}),cnt
print('MODULAR_ALL_PRIMITIVE_ROOTS_PASS: anchored=',sum(cnt.values()),'rank=',dict(sorted(cnt.items())))
print('All primitive roots modulo 1201; degree-8 coefficient bound at most 6; hence exact complex rank.')
