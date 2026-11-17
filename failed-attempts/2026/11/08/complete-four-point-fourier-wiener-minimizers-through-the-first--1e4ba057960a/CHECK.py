#!/usr/bin/env python3
"""Exact rational interval verification of all four-subset Fourier L1 minimizers, 8 <= N <= 17.
No third-party dependencies. Python 3.9+ required.
"""
from fractions import Fraction as Q
from math import factorial, gcd, isqrt, comb
from itertools import combinations

SCALE=10**13

def atan_bounds(d, K):
    s=sum(((-1)**j * Q(1, (2*j+1)*d**(2*j+1)) for j in range(K)),Q(0))
    rem=Q(1,(2*K+1)*d**(2*K+1))
    return (s,s+rem) if K%2==0 else (s-rem,s)

a,b=atan_bounds(5,32)
c,d=atan_bounds(239,11)
PI_LO=16*a-4*d
PI_HI=16*b-4*c
assert Q(3,1)<PI_LO<PI_HI<Q(22,7)
PI=(PI_LO+PI_HI)/2
REMAINDER=Q(22,7)**38/factorial(38) # cosine truncated at power 36

def ceilfrac(x): return -((-x.numerator)//x.denominator)
def floorfrac(x): return x.numerator//x.denominator

def cosine_fixed(N, r):
    t=min(r%N, (-r)%N)
    if t==0: return SCALE,SCALE
    weight=Q(2*t,N)
    x=weight*PI
    term=Q(1)
    poly=term
    for j in range(1,19):
        term *= -x*x/Q((2*j-1)*(2*j))
        poly+=term
    err=REMAINDER+weight*(PI_HI-PI_LO)/2
    return floorfrac((poly-err)*SCALE),ceilfrac((poly+err)*SCALE)

def orbit(N,C):
    return {tuple(sorted((t+d*c)%N for c in C))
            for t in range(N) for d in range(1,N) if gcd(d,N)==1}

def d_bounds(N,C,cos):
    lower=upper=0
    for k in range(1,N):
        s_lo=4*SCALE; s_hi=s_lo
        for a,b in combinations(C,2):
            lo,hi=cos[(k*(b-a))%N]
            s_lo += 2*lo; s_hi += 2*hi
        assert s_hi>=0
        low_root=isqrt(max(0,s_lo)*SCALE)
        high_root=isqrt(s_hi*SCALE)+1
        lower+=low_root;upper+=high_root
    return lower,upper

def expected(N):
    if N%4==0:return tuple(range(0,N,N//4))
    if N%2==0:return (0,1,N//2,N//2+1)
    return (0,1,2,3)

def verify():
    total_orbits=0
    total_sets=0
    lines=[]
    for N in range(8,18):
        cos=[cosine_fixed(N,r) for r in range(N)]
        unseen=set(combinations(range(N),4))
        classes=[]
        while unseen:
            C=min(unseen)
            o=orbit(N,C)
            assert o<=unseen or not (o-unseen) # orbit may include removed only if bug
            assert o<=unseen
            unseen.difference_update(o)
            L,U=d_bounds(N,C,cos)
            classes.append((C,len(o),L,U))
        assert sum(size for _,size,_,_ in classes)==comb(N,4)
        total_sets += comb(N,4);total_orbits+=len(classes)
        good_orbit=orbit(N,expected(N))
        winners=[v for v in classes if v[0] in good_orbit]
        assert len(winners)==1
        winner=winners[0]
        assert all(winner[3]<v[2] for v in classes if v!=winner), (N,winner,classes)
        lower_others=min((v[2] for v in classes if v!=winner),default=None)
        assert lower_others is not None
        # Bound minimum in outward milli-units for human-readable summary.
        lines.append((N,len(classes),winner[1],winner[2],winner[3],lower_others))
    for N,count,size,L,U,other in lines:
        print('N=%d orbits=%d minimizing_sets=%d D_in=[%s,%s] strict_gap_at_least=%s' %
              (N,count,size,format(L/SCALE,'.10f'),format(U/SCALE,'.10f'),format((other-U)/SCALE,'.10f')))
    print('CHECK_OK orders=8..17 sets=%d affine_orbits=%d strict_minimum_all_orders=1'% (total_sets,total_orbits))

if __name__=='__main__':verify()
