#!/usr/bin/env python3
"""Directly compare size-n weak-order theory sets to a transfer generating function."""
from itertools import product

def comps(n):
    if n==0:
        yield ()
        return
    for i in range(1,n+1):
        for c in comps(n-i):
            yield (i,)+c

def coefficients(k, limit):
    # 1/(1-A-B): restricted compositions of parts 1..k.
    all_reps=[0]*(limit+1); all_reps[0]=1
    for n in range(1,limit+1):
        all_reps[n]=sum(all_reps[n-a] for a in range(1,min(k,n)+1))
    # 1/(1-A): compositions of parts 1..k-1.
    unsat=[0]*(limit+1);unsat[0]=1
    for n in range(1,limit+1):
        unsat[n]=sum(unsat[n-a] for a in range(1,min(k-1,n)+1))
    # all theories present at size n: no capped part or >=1 saturated capped part
    return [all_reps[n]-unsat[n]+sum(all_reps[i]-unsat[i] for i in range(n))+(unsat[n] if n else 0) for n in range(limit+1)]

for k in (2,3,4,5):
    max_n=12 if k<5 else 11
    predictions=coefficients(k,max_n)
    for n in range(1,max_n+1):
        signatures={(tuple(min(k,x) for x in c)) for c in comps(n)}
        assert predictions[n]==len(signatures),(k,n,predictions[n],len(signatures))
    print('WIDTH',k,'ORDER_N_THEORY_COUNTS_1_TO_'+str(max_n),','.join(str(x) for x in predictions[1:]))
print('ORDER_SPECTRUM_FINITE_CHECKS_PASS')
