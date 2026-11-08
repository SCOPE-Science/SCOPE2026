#!/usr/bin/env python3
"""Exact determinant certificate for a two-parameter 4D zonotope volume inequality.

Run: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

E=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
def diff(a,b): return tuple(x-y for x,y in zip(a,b))
G=[E[0],E[1],E[2],diff(E[1],E[3]),diff(E[2],E[3])]
w=diff(E[0],E[3]);v=diff(E[1],E[2]);h0=(1,-1,-1,0)
BASES=[G,G+[w],G+[v],G+[w,v]]
PERMS=[(p,(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))) for p in permutations(range(4))]

def det4(cols):
    return sum(sign*cols[0][perm[0]]*cols[1][perm[1]]*cols[2][perm[2]]*cols[3][perm[3]] for perm,sign in PERMS)

def slope_formula(i,z):
    q=abs(z);u=abs(z-1);r=abs(z-2);s=abs(z+1)
    return [6+q+2*u+r,12+3*q+3*u+r+s,10+3*q+2*u+3*r,18+5*q+5*u+3*r+3*s][i]

def phase(i):
    return [F(-2),F(-1,2),F(1,2),F(3,2),F(3)][i]

def defect_formula(z,t):
    if z<=-1: return 4*t*t*(2*z-7)
    if z<=0: return -4*t*(t*(2*z*z-6*z+1)-2*(1+z))
    if z<=1: return 4*t*(2-6*z-t*(1+7*z))
    if z<=2: return 4*t*(t*(2*z*z-z-9)+4*z-8)
    return -4*t*t*(2*z-1)

minors=[]
for vectors in BASES:
    const=sum(abs(det4([vectors[j] for j in I])) for I in combinations(range(len(vectors)),4))
    coeffs=[]
    for I in combinations(range(len(vectors)),3):
        three=[vectors[j] for j in I]
        coeffs.append((det4(three+[h0]),det4(three+[E[3]])))
    minors.append((const,coeffs))
assert [const for const,_ in minors]==[4,12,8,24]
nonzero_roots={F(-a,b) for _,coeffs in minors for a,b in coeffs if b}
assert nonzero_roots=={-1,0,1,2},nonzero_roots
assert [sum(abs(a) for a,b in coeffs) for _,coeffs in minors]==[10,18,18,32]
assert [sum(abs(a+b) for a,b in coeffs) for _,coeffs in minors]==[8,18,16,32]

# Each actual minor is linear in z and has no breakpoint outside the four
# roots above. Its summed absolute value is therefore affine on each of
# the five open chambers; two exact evaluations certify the full formula.
for j in range(5):
    lo,hi=([(-5,-1),(-1,0),(0,1),(1,2),(2,5)])[j]
    for z in (F(2*lo+hi,3),F(lo+2*hi,3)):
        for i,(const,coeffs) in enumerate(minors):
            assert sum(abs(a+z*b) for a,b in coeffs)==slope_formula(i,z)

checks=0
for z in [F(k,7) for k in range(-28,29)]+[F(-1),F(0),F(1),F(2),F(1,13),F(-1,8),F(1,3)]:
    for t in [F(0),F(1,7),F(1,2),F(1),F(3,2),F(2),F(3),F(7)]:
        volumes=[const+t*sum(abs(a+z*b) for a,b in coeffs) for const,coeffs in minors]
        A,AB,AC,ABC=volumes
        assert volumes==[const+t*slope_formula(i,z) for i,(const,_) in enumerate(minors)]
        assert A*ABC-AB*AC==defect_formula(z,t),(z,t,volumes)
        checks+=1
assert defect_formula(F(0),F(1))==4
assert defect_formula(F(0),F(2))==0
assert defect_formula(F(0),F(3))<0
assert defect_formula(F(1,13),F(1))==0
print(f'VERIFY_OK {checks} exact rational (z,t) full-minor checks; five affine chambers certified by determinant roots')
