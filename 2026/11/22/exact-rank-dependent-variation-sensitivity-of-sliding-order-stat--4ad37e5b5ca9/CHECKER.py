#!/usr/bin/env python3
"""Exact integer checks for the sharp finite-path running-quantile variation law.
No external dependencies. Finite tests supplement, not replace, the proof.
"""
from itertools import permutations
from random import Random

def quantile_filter(v, radius, rank):
    n = len(v)
    return [sorted(v[max(0,min(n-1,i+j))] for j in range(-radius,radius+1))[rank-1]
            for i in range(n)]

def tv(v):
    return sum(abs(a-b) for a,b in zip(v,v[1:]))

def witness(radius, rank):
    r=radius; w=2*r+1; n=w+1
    if rank > r+1:
        z = witness(r,w+1-rank)
        return [-v for v in z]
    q=rank; s=r-q+1
    z=list(range(s+1))
    z += [s+2+2*j for j in range(q-1)]
    z += [s+1+2*j for j in range(q)]
    z += list(range(r+q+1,n))
    assert sorted(z)==list(range(n))
    return z

def gain_from_selected_base(x,r,q,cut):
    n=len(x)
    selected=[]
    for i in range(n):
        wi=[max(0,min(n-1,i+j)) for j in range(-r,r+1)]
        selected.append(sorted(wi,key=lambda t:x[t])[q-1])
    return tv([int(idx>=cut) for idx in selected])

def main():
    for r in range(1,65):
        for q in range(1,2*r+2):
            z=witness(r,q)
            n=len(z); cut=r+1
            g=gain_from_selected_base(z,r,q,cut)
            expected=2*min(q-1,2*r+1-q)+1
            assert g==expected,(r,q,g,expected)
            h=[int(i>=cut) for i in range(n)]
            eps=1/4
            y=[z[i]+eps*h[i] for i in range(n)]
            actual=tv([a-b for a,b in zip(quantile_filter(y,r,q),quantile_filter(z,r,q))])
            assert abs(actual/eps-expected)<1.e-10,(r,q,actual,expected)
    print('CONSTRUCTIVE_SHARPNESS_ALL_RADII_1_TO_64_EXACT_SELECTOR_PASS')

    for n in range(4,8):
        for r in range(1,4):
            w=2*r+1
            for q in range(1,w+1):
                expected=2*min(q-1,w-q)+1
                highest=0
                for p in permutations(range(n)):
                    for cut in range(1,n):
                        highest=max(highest,gain_from_selected_base(p,r,q,cut))
                        assert highest<=expected,(n,r,q,highest,expected)
                if n>=w+1:assert highest==expected,(n,r,q,highest,expected)
    print('EXHAUSTIVE_SMALL_PATH_SELECTOR_UPPER_AND_SHARPNESS_PASS')

    gen=Random(249417)
    for it in range(3000):
        n=gen.randint(3,40)
        r=gen.randint(1, min(9,n+3))
        q=gen.randint(1,2*r+1)
        x=[gen.randint(-30,30) for _ in range(n)]
        y=[gen.randint(-30,30) for _ in range(n)]
        lhs=tv([a-b for a,b in zip(quantile_filter(x,r,q),quantile_filter(y,r,q))])
        rhs=(2*min(q-1,2*r+1-q)+1)*tv([a-b for a,b in zip(x,y)])
        assert lhs<=rhs,(it,n,r,q,lhs,rhs)
    print('RANDOM_TWO_INPUT_INTEGER_TV_BOUND_3000_PASS')
    print('ALL_RUNNING_RANK_VARIATION_CHECKS_PASS')

if __name__=='__main__':main()
