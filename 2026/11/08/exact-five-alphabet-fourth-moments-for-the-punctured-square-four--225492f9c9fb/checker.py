#!/usr/bin/env python3
"""Exact two-dimensional fourth-moment certificates, stdlib only.

All arrays in the stated finite phase alphabets are exhausted after
three independent phase symmetries are normalized. No floating-point
arithmetic or heuristic optimization is used.
"""
from itertools import product
from pathlib import Path
from collections import defaultdict
import json

POSITIONS = tuple((a,b) for a in (0,1,2) for b in (0,1,2) if (a,b)!=(1,1))
FREE = (2,4,5,6,7)
FROZEN = (0,1,3)
DIFFERENCES = sorted({(b[0]-a[0],b[1]-a[1])
                      for a in POSITIONS for b in POSITIONS if a != b})
POSITIVE_SHIFTS = tuple(d for d in DIFFERENCES if d > (0,0))
SHIFTS = {d: tuple((i,j) for i,a in enumerate(POSITIONS)
                  for j,b in enumerate(POSITIONS)
                  if (b[0]-a[0],b[1]-a[1]) == d)
          for d in POSITIVE_SHIFTS}
SUMS = defaultdict(list)
for i,a in enumerate(POSITIONS):
    for j,b in enumerate(POSITIONS):
        SUMS[(a[0]+b[0],a[1]+b[1])].append((i,j))

ROOTS = {
    2: ((1,0),(-1,0)),
    3: ((1,0),(0,1),(-1,-1)),
    4: ((1,0),(0,1),(-1,0),(0,-1)),
    6: ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)),
}

def quadratic_sign(a,b):
    """Sign of a+b*sqrt(5), determined using integer arithmetic."""
    if b == 0:
        return (a>0)-(a<0)
    if a == 0:
        return (b>0)-(b<0)
    if (a>0)==(b>0):
        return (a>0)-(a<0)
    discr = a*a-5*b*b
    assert discr != 0  # sqrt(5) irrational, a,b nonzero integers
    return ((a>0)-(a<0)) if discr>0 else ((b>0)-(b<0))

def cmp(a,b):
    return quadratic_sign(a[0]-b[0],a[1]-b[1])

def modulus_squared(exponents, q):
    """Gaussian/Eisenstein norm of a sum of roots, for q in 2,3,4,6."""
    assert q in ROOTS
    x=y=0
    for k in exponents:
        a,b=ROOTS[q][k%q]
        x+=a; y+=b
    return (x*x+y*y-(x*y if q in (3,6) else 0),0)

# q=5 norm must be computed as a half-integer pair before summation.
def doubled_modulus_squared(exponents,q):
    if q==5:
        hist = [0]*5
        for k in exponents: hist[k%5]+=1
        B = sum(n*n for n in hist)
        A = sum(hist[i]*hist[(i+1)%5] for i in range(5))
        C = sum(hist[i]*hist[(i+2)%5] for i in range(5))
        return 2*B-A-C, A-C
    v = modulus_squared(exponents,q)
    return 2*v[0],0

def fourth_moment_autocorr(e,q):
    value = (64,0)
    for pairs in SHIFTS.values():
        x,y = doubled_modulus_squared([(e[j]-e[i])%q for i,j in pairs],q)
        value = (value[0]+x,value[1]+y)
    return value

def fourth_moment_convolution(e,q):
    # Sum absolute squares of Fourier coefficients of P^2.
    first=second=0
    for pairs in SUMS.values():
        x,y=doubled_modulus_squared([(e[i]+e[j])%q for i,j in pairs],q)
        assert x%2==y%2
        first += x
        second += y
    assert first%2==second%2==0
    return first//2, second//2

def run():
    catalog=json.loads(Path(__file__).with_name('optimizer_catalog.json').read_text())
    assert tuple(tuple(x) for x in catalog['coords']) == tuple((i-1,j-1) for i,j in POSITIONS)
    assert catalog['free_indices']==list(FREE)
    assert catalog['gauge_zero_indices']==list(FROZEN)
    assert len(POSITIVE_SHIFTS)==12
    checked=0
    for q in (2,3,4,5,6):
        data=catalog['per_phase_alphabet'][str(q)]
        minv=maxv=None
        optimizers=[]
        for free in product(range(q),repeat=len(FREE)):
            e=[0]*8
            for i,k in zip(FREE,free): e[i]=k
            via_cor=fourth_moment_autocorr(e,q)
            via_conv=fourth_moment_convolution(e,q)
            assert via_cor==via_conv, (q,free,via_cor,via_conv)
            checked+=1
            if minv is None or cmp(via_cor,minv)<0:
                minv=via_cor;optimizers=[list(free)]
            elif cmp(via_cor,minv)==0:
                optimizers.append(list(free))
            if maxv is None or cmp(via_cor,maxv)>0:
                maxv=via_cor
        assert minv == tuple(data['minimum_pair_Z_sqrt5'])
        assert maxv == tuple(data['maximum_pair_Z_sqrt5'])
        assert optimizers == data['normalized_optima']
        assert len(optimizers)*q**3 == data['full_optima_count']
        assert q**5 == data['scanned_normalized']
        print('q={} cases={} min={}+({})sqrt(5) normalized={} all={}'.format(q,q**5,minv[0],minv[1],len(optimizers),len(optimizers)*q**3))
    assert checked==12200
    print('HOLLOW_SQUARE_FOURTH_MOMENT_PASS checked={} direct_vs_convolution=all'.format(checked))

if __name__ == '__main__':
    run()
