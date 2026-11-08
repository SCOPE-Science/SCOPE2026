#!/usr/bin/env python3
"""Exact rational verification of the one-nodal quartic del Pezzo chamber census.

Run: python3 verify.py    (Python 3.9+, standard library only).
The algebraic-geometric exhaustion of negative curves is proved separately.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

# (d,m1,...,m5) represents the divisor dH - sum_i mi Ei.
def exceptional(i):
    a = [0] * 6
    a[i + 1] = -1
    return tuple(a)
def line(i,j):
    a = [0] * 6
    a[0] = 1
    a[i + 1] = a[j + 1] = 1
    return tuple(a)
def triple_line():
    return (1,1,1,1,0,0)
def intersection(a,b):
    return a[0]*b[0] - sum(a[i]*b[i] for i in range(1,6))

curves = [(f'E{i+1}',exceptional(i)) for i in range(5)]
curves += [(f'L{i+1}{j+1}',line(i,j)) for i in range(3) for j in (3,4)]
curves += [('L45',line(3,4)), ('R',triple_line())]
assert len(curves) == 13 and [intersection(v,v) for _,v in curves] == [-1]*12+[-2]
M = [[intersection(u,v) for _,v in curves] for _,u in curves]

# Negative-definite iff the opposite matrix has positive sequential Schur pivots.
def negative_definite(ids):
    a = [[-Fraction(M[i][j]) for j in ids] for i in ids]
    n = len(a)
    for k in range(n):
        pivot = a[k][k]
        if pivot <= 0:
            return False
        for i in range(k+1,n):
            for j in range(i,n):
                v = a[i][j]-a[i][k]*a[k][j]/pivot
                a[i][j] = a[j][i] = v
    return True

count = Counter()
for mask in range(1<<len(curves)):
    ids = [i for i in range(len(curves)) if mask & (1<<i)]
    if negative_definite(ids):
        count[(int(12 in ids),len(ids))] += 1

finite = [count[(0,d)] for d in range(7)]
infinite = [count[(1,d)] for d in range(7)]
assert finite == [1,12,46,72,43,4,0]
assert infinite == [0,1,12,40,44,10,0]
assert sum(finite)==178 and sum(infinite)==107
assert [a+b for a,b in zip(finite,infinite)]==[1,13,58,112,87,14,0]

# Independent symbolic derivation via the cross-line independence polynomial.
def add(a,b):
    return [sum(x) for x in __import__('itertools').zip_longest(a,b,fillvalue=0)]
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]+=x*y
    return r
def power(a,n):
    r=[1]
    for _ in range(n):r=mul(r,a)
    return r
def scale(a,c):return [c*x for x in a]
def shift(a,k):return [0]*k+a

def F(m):
    return add(add(scale(power([1,1],m),2),[-1]),[0,0,m])
def H(m):
    return add(add(F(m),shift(scale(power([1,1],m),2),1)),[0,0,1])
def G(m):
    return add(mul([1,1],F(m)),add(shift(scale(power([1,1],m),2),1),[0,0,1]))
P0 = [0]
for a in range(4):
    P0=add(P0,shift(scale(G(3-a),comb(3,a)),a))
P1=shift(add(G(3),shift(scale(H(2),3),1)),1)
assert P0[:7] == finite and not any(P0[7:]), (P0,finite)
assert (P1 + [0]*max(0,7-len(P1)))[:7] == infinite and not any(P1[7:]), (P1,infinite)

print('CURVES',len(curves),'SUBSETS',2**len(curves))
print('FINITE_SUPPORT_POLYNOMIAL',finite[:6])
print('INFINITE_SUPPORT_POLYNOMIAL',infinite[:6])
print('TOTAL_SUPPORT_POLYNOMIAL',[a+b for a,b in zip(finite,infinite)][:6])
print('TOTAL_CHAMBERS',sum(finite)+sum(infinite))
print('ALL_CHECKS_PASSED')
