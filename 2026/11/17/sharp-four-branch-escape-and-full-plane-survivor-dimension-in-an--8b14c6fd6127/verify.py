#!/usr/bin/env python3
"""Exact-rational checks for a four-branch return map, its inverse branches,
edge values, and finite-level survivor lengths. No external dependencies."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt,log

def H(y,c,A,B):
    return c*abs(c*abs(y)-A)-B

def inverse(t,c,A,B,sig,tau):
    return sig*(A+tau*(t+B)/c)/c

def check(c,u):
    A=1+u; B=2-u
    U=(c*A+B)/(c*c-1)
    assert 0<A and 0<B and U<B and c*A-B>U
    assert U>A/c
    assert H(-U,c,A,B)==U
    assert H(U,c,A,B)==U
    assert H(-A/c,c,A,B)==-B
    assert H(A/c,c,A,B)==-B
    assert H(Q(0),c,A,B)==c*A-B
    for t in [-U,-U/2,Q(0),U/2,U]:
        inv=[inverse(t,c,A,B,s,tau) for s,tau in product([-1,1],[-1,1])]
        assert len(set(inv))==4
        assert all(-U<=y<=U and H(y,c,A,B)==t for y in inv)
        assert len(set((y>0,abs(y)>A/c) for y in inv))==4
    for n in range(1,5):
        # Cylinders of H^{-n}([-U,U]) obtained via all 4^n inverse compositions.
        seg=[(-U,U)]
        for k in range(n):
            new=[]
            for left,right in seg:
                for s,tau in product([-1,1],[-1,1]):
                    x=inverse(left,c,A,B,s,tau)
                    y=inverse(right,c,A,B,s,tau)
                    new.append((min(x,y),max(x,y)))
            seg=new
        # Correct n-level inverse construction; list starts from J and prepends inverse branches.
        seg.sort()
        assert len(seg)==4**n
        assert all(seg[i][1]<seg[i+1][0] for i in range(len(seg)-1))
        length=sum((r-l for l,r in seg),Q(0))
        assert length==2*U*Q(4**n,c**(2*n))
    return U

count=0
for c in map(Q,[3,4,5,7,11]):
    for u in [Q(0),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10),Q(1)]:
        check(c,u);count+=1
print('EXACT_FOUR_BRANCH_OK', 'parameter_phases='+str(count), 'levels=1..4', 'max_cylinders=256')
# Confirm sharp boundary numerically using exact rational c=27/10 < 1+sqrt(3).
c=Q(27,10);u=Q(1); A=1+u;B=2-u;U=(c*A+B)/(c*c-1)
assert U>=B
print('SHARP_THRESHOLD_WITNESS_OK', 'c=27/10', 'phase=1', 'B_minus_U='+str(B-U))
# Confirm upper formula for an external point past the canonical interval.
for c in map(Q,[3,4,5]):
 for u in [Q(0),Q(1,2),Q(1)]:
  A=1+u;B=2-u; U=(c*A+B)/(c*c-1)
  for delta in [Q(1,10),Q(1)]:
   assert H(U+delta,c,A,B)==U+c*c*delta
   assert H(-U-delta,c,A,B)==U+c*c*delta
print('ESCAPE_IDENTITIES_OK')
