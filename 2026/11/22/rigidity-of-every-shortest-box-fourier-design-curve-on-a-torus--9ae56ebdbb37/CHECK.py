#!/usr/bin/env python3
"""Exact integer checks for Fourier design-curve extremal winding classification.
The global proof is analytic; this bounded census is diagnostic only.
"""
from itertools import product, permutations
from math import isqrt

def powers(t, d):
    b = t+1
    return tuple(b**j for j in range(d))

def is_box_design(t, v):
    # For a straight integer-winding curve, integrals vanish iff no
    # nonzero box-frequency m annihilates the winding vector.
    for m in product(range(-t, t+1), repeat=len(v)):
        if any(m) and sum(x*y for x,y in zip(m,v)) == 0:
            return False
    return True

def has_complete_digits(t, v):
    s = [sum(a*w for a,w in zip(digits,v)) for digits in
         product(range(t+1), repeat=len(v))]
    return sorted(s) == list(range((t+1)**len(v)))

def run():
    cases = [(2,t) for t in range(1,8)]+[(3,t) for t in range(1,5)]+[(4,t) for t in (1,2)]
    total = good = 0
    for d,t in cases:
        expected = powers(t,d)
        bound = sum(v*v for v in expected)
        candidates=[]
        for v in product(range(isqrt(bound)+1), repeat=d):
            if sum(x*x for x in v) == bound:
                candidates.append(v)
        hits=[v for v in candidates if is_box_design(t,v)]
        target=set(permutations(expected))
        assert set(hits)==target,(d,t,bound,hits,target)
        for v in target:
            assert has_complete_digits(t,v)
        total += len(candidates)
        good += len(hits)
        print('d=%d t=%d L2=%d sphere_vectors=%d design_minima=%d'%(d,t,bound,len(candidates),len(hits)))
    print('PASS: cases=%d sphere_vectors=%d design_minima=%d; box-frequency range tests vary by case'%(len(cases),total,good))

if __name__ == '__main__':
    run()
