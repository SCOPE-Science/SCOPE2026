#!/usr/bin/env python3
"""Exact rational certificates and reproducible examples for a periodic
averaged-hat interpolation approximation inequality.
Python standard library only. Infinite proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

def coefficient_on_interval(a, left, right):
    n = len(a) - 1
    h = right - left
    return [sum(a[i] * comb(i,j) * left**(i-j) * h**j for i in range(j,n+1)) for j in range(n+1)]

def bernstein(a, left, right):
    a = coefficient_on_interval(a, left, right)
    n = len(a)-1
    return [sum(a[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]

# F(s) is the upper bound for jumps in consecutive cells with
# 0 <= s <= 1/2, 0 <= v <= 1/2.
F=[Q(5,12),Q(1,6),-Q(13,12),Q(2,3),Q(1,3)]
# G(v) bounds jumps in consecutive cells with s >= 1/2, v >= 1/2.
G=[Q(1,2),-Q(4,3),Q(35,12),-Q(2),Q(1,3)]

def deficit(a):
    ans=[-x for x in a]
    ans[0] += Q(3,7)
    return ans
assert min(bernstein(deficit(F),Q(0),Q(1,4))) == Q(1,672)
assert min(bernstein(deficit(F),Q(1,4),Q(1,2))) == Q(47,1792)
assert min(bernstein(deficit(G),Q(1,2),Q(3,4))) == Q(47,1792)
assert min(bernstein(deficit(G),Q(3,4),Q(1))) == Q(1,672)

# K(s,v): magnitude of negative overlap of two oriented jump residuals,
# s in [1/2,1], v in [0,1/2], t=1+v.
K={(4,1):Q(1,3),(4,0):-Q(1,6),
   (3,1):-Q(1,2),(3,0):Q(1,4),
   (2,1):Q(1,2),(2,0):-Q(1,4),
   (1,4):-Q(1,3),(1,3):Q(5,6),(1,2):-Q(1),
   (1,1):Q(1,6),(1,0):Q(1,6),
   (0,4):Q(1,6),(0,3):-Q(5,12),(0,2):Q(1,2),(0,1):-Q(1,4)}

def tensor_bernstein(coeff, s0, s1, v0, v1, ns=4, nv=4):
    converted={}
    for (i,j),a in coeff.items():
        for k in range(i+1):
            for l in range(j+1):
                converted[(k,l)]=converted.get((k,l),Q(0)) + (a*comb(i,k)*s0**(i-k)*(s1-s0)**k
                    *comb(j,l)*v0**(j-l)*(v1-v0)**l)
    return [sum(converted.get((i,j),Q(0))*Q(comb(k,i),comb(ns,i))
                *Q(comb(l,j),comb(nv,j))
                for i in range(k+1) for j in range(l+1))
            for k in range(ns+1) for l in range(nv+1)]
D={key:-val for key,val in K.items()}
D[(0,0)]=D.get((0,0),Q(0))+Q(1,21)
b=tensor_bernstein(D,Q(1,2),Q(1),Q(0),Q(1,2))
assert len(b)==25 and min(b)==Q(1,1344)

# Same-cell polynomial identity, written directly with rational arithmetic.
def same_cell_q(s,t):
    a=max(Q(0),min(t,Q(1,2))-s)
    z=max(Q(0),t-max(s,Q(1,2)))
    d=t-s
    cross=a*(d-(t*t-s*s)/2)+z*(t*t-s*s)/2
    return d-2*cross+Q(2,3)*(a*a+z*z)+a*z/3
for i in range(1,30):
  for j in range(i+1,31):
    s=Q(i,32);t=Q(j,32)
    if s<=Q(1,2)<=t:
        a=Q(1,2)-s;z=t-Q(1,2);d=a+z
        assert same_cell_q(s,t)==d-Q(7,12)*d*d-(d-Q(1,4))*(a-z)**2
assert same_cell_q(Q(1,14),Q(13,14))==Q(3,7)

def intersection(a,b,c,d):
    return max(Q(0),min(b,d)-max(a,c))

def residual_energy(N,s,t):
    assert N>=6 and 0 <= s < t < N
    vals=[sum(intersection(Q(k)-Q(1,2),Q(k)+Q(1,2),s+m*N,t+m*N)
              for m in (-1,0,1)) for k in range(N)]
    square=sum((vals[k]**2+vals[k]*vals[(k+1)%N]+vals[(k+1)%N]**2)/3
               for k in range(N))
    cross=Q(0)
    for k in range(N):
      for m in (-1,0,1):
        a=max(Q(k),s+m*N);b=min(Q(k+1),t+m*N)
        if a>=b:continue
        y=a-k;z=b-k
        cross+=vals[k]*(z-y)+(vals[(k+1)%N]-vals[k])*(z*z-y*y)/2
    return (t-s)-2*cross+square

checks=0
for N in (6,7,8,10):
    for i in range(0,18):
      s=Q(i,19)
      for k in range(1,N*12):
        d=Q(k,12)
        if d>N/2 or s+d>=N:continue
        q=residual_energy(N,s,s+d)
        assert q<=Q(3,7), (N,s,d,q)
        checks+=1
    for cell in range(N):
      assert residual_energy(N,Q(cell)+Q(1,14),Q(cell)+Q(13,14))==Q(3,7)
      checks+=1
print('PASS: exact Bernstein positivity, same-cell identity, witness, and',checks,'rational pulse comparisons')
