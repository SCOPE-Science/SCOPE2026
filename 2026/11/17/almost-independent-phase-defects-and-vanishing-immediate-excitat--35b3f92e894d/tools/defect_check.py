#!/usr/bin/env python3
"""Direct arithmetic checks of local excitation defects on small Boolean cubes.
No external packages are required. All counts are exact integers.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

def neighbor_lists(d):
    return [tuple(v^(1<<j) for j in range(d)) for v in range(1<<d)]

def defect_vector(colors, neighbors):
    return tuple(int(all(colors[w] != (colors[v]+1)%3 for w in neighbors[v]))
                 for v in range(len(colors)))

def update(colors, neighbors):
    return tuple(2 if c==1 else 0 if c==2 else int(any(colors[w]==1 for w in neighbors[v]))
                 for v,c in enumerate(colors))

def check(d):
    n=1<<d
    hist=Counter(); q1=Counter(); q2=Counter(); waves=0; witness=None
    nb=neighbor_lists(d)
    for c in product(range(3),repeat=n):
        y=defect_vector(c,nb)
        k=sum(y); hist[k]+=1
        if k==0:
            waves+=1
            if witness is None: witness=''.join(map(str,c))
        # Independent direct 3-step dynamical check
        a=update(c,nb); b=update(a,nb); c3=update(b,nb)
        three=(c3==c and a!=c)
        assert three==(k==0), (d,c,k,three)
    total=3**n
    p=Fraction(2,3)**d
    mean=Fraction(sum(k*z for k,z in hist.items()),total)
    variance=Fraction(sum(k*k*z for k,z in hist.items()),total)-Fraction(sum(k*z for k,z in hist.items()),total)**2
    expected_mean=n*p
    expected_variance=expected_mean+ n*p*p*Fraction(d*d-5*d-16,16)
    assert mean==expected_mean
    assert variance==expected_variance
    # Pair correlations via direct enumeration, distinguished vertices 0 and w.
    for distance in (1,2):
        if distance>d: continue
        w=(1<<distance)-1
        observed=Fraction(0)
        for c in product(range(3),repeat=n):
            y=defect_vector(c,nb)
            observed+=y[0]*y[w]
        observed/=total
        expected=p*p*(Fraction(3,4) if distance==1 else Fraction(9,8))
        assert observed==expected,(distance,observed,expected)
    print('d',d,'states',total,'waves',waves,'mean',expected_mean,'variance',expected_variance,'witness',witness,'histogram',dict(sorted(hist.items())))

if __name__=='__main__':
    for d in (1,2,3): check(d)
    for d in (4,8,16,32,64,128,256):
        n=1<<d; p=Fraction(2,3)**d
        mu=n*p; m=1+d+comb(d,2)
        polynomial=1+Fraction(7,4)*d+Fraction(17,8)*comb(d,2)
        assert polynomial>0
        print('bound_check d',d,'mean_float',float(mu) if d<64 else 'large',
              'TV_prefactor_float',float(Fraction(8,9)**d*polynomial),
              'packing_size_lower_bound',n//m)
    print('ALL_CHECKS_PASS')
