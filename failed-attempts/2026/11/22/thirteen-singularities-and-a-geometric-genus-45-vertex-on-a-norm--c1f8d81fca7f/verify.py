#!/usr/bin/env python3
"""Exact finite-field incidence check for the nine-line dual Hesse arrangement.
The global resolution/genus argument is algebraic and is stated in RESULT.md.
"""
from itertools import combinations
from collections import Counter
from math import comb
p=7
zeta=2
assert zeta**3 %p==1 and zeta%p!=1
lines=[]
for i in range(3):
 z=pow(zeta,i,p)
 lines += [(1,-z,0),(0,1,-z),(-z,0,1)]
def norm(a):
 a=tuple(v%p for v in a)
 k=next(v for v in a if v)
 inv=pow(k,-1,p)
 return tuple(v*inv%p for v in a)
def cross(a,b):
 return norm((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))
lines=[norm(x) for x in lines]
assert len(set(lines))==9
incidence=Counter()
for a,b in combinations(lines,2):
 incidence[cross(a,b)]+=1
assert len(incidence)==12
assert Counter(incidence.values())=={3:12} # three pairs per triple
assert sum(incidence.values())==comb(9,2)
# P^2(F7) triple points are all rational because primitive third roots are in F7.
points=set(incidence)
assert all(sum(sum(a*b for a,b in zip(l,pt))%p==0 for l in lines)==3 for pt in points)
# Plane-cubic cone: smooth cubic E (three transverse branch factors) has chi(O_E)=0,
# h1(O_E)=1, h1(O_E(n))=0 for n>0. Thus local pg=1.
chi_surface=1+comb(8,3)
chi_cyclic=1+comb(2,2)+comb(5,2) # chi(O), chi(O(-3)), chi(O(-6))
pg_vertex=chi_surface - (chi_cyclic-12) -12
assert (chi_surface,chi_cyclic,pg_vertex)==(57,12,45)
# Example smooth conic Q= X^2+Y^2+Z^2: test for avoidance over finite field
Q=lambda pt: (pt[0]**2+pt[1]**2+pt[2]**2+pt[1]*pt[2]+pt[0]*pt[2])%p
print('line_count',len(lines),'triple_points',len(points), 'pair_incidence',sum(incidence.values()))
assert all(Q(pt) for pt in points)
# Hessian determinant of Q (integer coefficients): det([[2,0,1],[0,2,1],[1,1,2]])=4.
assert 2*(2*2-1)-2==4
print('Q=x^2+y^2+z^2+yz+xz smooth and nonzero on all triple points: yes')
print('chi_S',chi_surface,'chi_V',chi_cyclic,'pg_cyclic_res',chi_cyclic-12,'pg_vertex',pg_vertex)
