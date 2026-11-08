#!/usr/bin/env python3
"""Independently enumerate small categorical cylinder-cell shattering counts."""
from itertools import product, combinations
from math import factorial, comb, prod

def theoretical(qs, m):
    p=prod(qs)
    if m==0: return 1
    if m==1: return p
    if m==2: return comb(p,2) if p>2 else 0
    if m>len(qs): return 0
    return sum((-1)**j*comb(m,j)*prod(q**m-j*q*(q-1) for q in qs)
               for j in range(m+1))//factorial(m)

def brute(qs, max_m):
    points=list(product(*(range(q) for q in qs)))
    faces=[]
    for f in product(*([None]+list(range(q)) for q in qs)):
        mask=0
        for i,x in enumerate(points):
            if all(a is None or a==b for a,b in zip(f,x)):
                mask |=1<<i
        faces.append(mask)
    got=[]
    for m in range(max_m+1):
        ct=0
        for S in combinations(range(len(points)),m):
            smask=sum(1<<x for x in S)
            traces={f&smask for f in faces}
            if len(traces)==(1<<m):ct+=1
        want=theoretical(qs,m)
        if ct!=want:
            raise AssertionError((qs,m,ct,want))
        got.append(ct)
    return got

cases=[(2,), (3,), (4,), (5,), (2,2), (2,3), (2,4), (3,3),
       (2,2,2), (2,2,3), (2,3,3), (2,2,2,2), (2,2,2,3)]
all_supports=0
for qs in cases:
    P=prod(qs); max_m=min(P, 5 if P<=12 else 4)
    got=brute(qs,max_m)
    all_supports+=sum(comb(P,k) for k in range(max_m+1))
    print(f'{qs}: counts through {max_m}: {got}')
assert theoretical((2,2,2),3)==8
assert theoretical((3,3,3),3)==216
assert theoretical((2,2,2,2),4)==16
assert theoretical((2,3,4),3)==(2*1)*(3*2)*(4*3)
print('ALL_CATEGORICAL_SUBCUBE_CHECKS_PASS',len(cases),'grids', all_supports,'supports')
