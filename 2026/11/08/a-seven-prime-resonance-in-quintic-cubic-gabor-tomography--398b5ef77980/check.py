#!/usr/bin/env python3
"""Exact root-count tests of the finite-field ambiguity-zero classification."""
from collections import Counter
from math import isqrt


def is_prime(p):
    return p>=2 and all(p%q for q in range(2,isqrt(p)+1))

def actual_zero_set(p,c,d):
    """Cyclotomic coefficient equality; no floating-point cancellation."""
    assert is_prime(p)
    f=[(c*x**5+d*x**3)%p for x in range(p)]
    zeros=set()
    for a in range(p):
        for b in range(p):
            counts=[0]*p
            for x in range(p):
                counts[(f[(x+a)%p]-f[x]-b*x)%p]+=1
            if all(count==1 for count in counts):
                zeros.add((a,b))
    return zeros

def predicted_zero_set(p,c,d):
    zeros={(0,b) for b in range(1,p)}
    if p in (2,3) or (p==5 and d==0) or (c==0 and d==0):
        return {(a,b) for a in range(p) for b in range(1,p)}
    if p==7 and c and d*pow(c,-1,7)%7 in (3,5,6):
        for a in range(1,p):
            if (d-5*c*a*a)%7==0:
                zeros.add((a,c*a%7))
                zeros.add((a,-c*a%7))
    return zeros

def run():
    for p in (2,3,5,7,11,13,17,19):
        ranks=Counter()
        for c in range(p):
            for d in range(p):
                actual=actual_zero_set(p,c,d)
                predicted=predicted_zero_set(p,c,d)
                assert actual==predicted, (p,c,d,actual^predicted)
                ranks[p*p-len(actual)]+=1
        print(p,dict(sorted(ranks.items())))
    for p,c,d in ((23,1,3),(23,2,7),(29,1,0),(31,5,8),(37,1,17)):
        actual=actual_zero_set(p,c,d)
        predicted=predicted_zero_set(p,c,d)
        assert actual==predicted,(p,c,d,actual^predicted)
        print(p,c,d,'rank',p*p-len(actual))
    print('QUINTIC_CUBIC_GABOR_RANK_CLASSIFICATION_PASS')
if __name__=='__main__':run()
