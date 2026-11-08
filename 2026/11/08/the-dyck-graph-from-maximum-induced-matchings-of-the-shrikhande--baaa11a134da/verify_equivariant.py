#!/usr/bin/env python3
"""Translation-equivariant construction of the Dyck exchange isomorphism.
Self-contained standard-library verification of the displayed two-orbit formula.
"""
from itertools import combinations, product
from collections import Counter
S = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
V=list(product(range(4),repeat=2))
add=lambda x,y:((x[0]+y[0])%4,(x[1]+y[1])%4)
def adjacent(x,y):return ((y[0]-x[0])%4,(y[1]-x[1])%4) in S
E=sorted((a,b) for a,b in combinations(V,2) if adjacent(a,b))
assert len(E)==48

def induced(M):
 U={v for e in M for v in e}
 return len(U)==2*len(M) and sum(adjacent(a,b) for a,b in combinations(sorted(U),2))==len(M)
M={frozenset(Q) for Q in combinations(E,3) if induced(Q)}
assert len(M)==32
assert not any(induced(Q) for Q in combinations(E,4))

def tr_edge(e,delta):return tuple(sorted((add(e[0],delta),add(e[1],delta))))
def tr_m(M,delta):return frozenset(tr_edge(e,delta) for e in M)
def tr_t(T,delta):return frozenset(add(v,delta) for v in T)
# Representatives of the two 16-element translation orbits of optimum matchings.
M0=frozenset({((0,1),(3,0)),((1,0),(1,3)),((2,2),(3,2))})
M1=frozenset({((0,0),(0,1)),((1,3),(2,0)),((2,2),(3,2))})
assert M0 in M and M1 in M
T={frozenset(c) for c in combinations(V,3) if all(adjacent(a,b) for a,b in combinations(c,2))}
assert len(T)==32
T0=frozenset({(0,0),(0,1),(3,0)})
T1=frozenset({(0,0),(0,1),(1,1)})
assert T0 in T and T1 in T
D=V
m0={tr_m(M0,x) for x in D};m1={tr_m(M1,x) for x in D}
t0={tr_t(T0,x) for x in D};t1={tr_t(T1,x) for x in D}
assert len(m0)==len(m1)==len(t0)==len(t1)==16
assert m0|m1==M and not m0&m1
assert t0|t1==T and not t0&t1
# Each edge of Shrikhande belongs to exactly two optimum induced matchings.
assert Counter(e for m in M for e in m)==Counter({e:2 for e in E})
# If x is the translation of M0 and y that of M1, their shared-edge
# condition is governed by these three differences y-x.
voltage_m={d for d in D if len(M0 & tr_m(M1,d))==1}
voltage_t={d for d in D if len(T0 & tr_t(T1,d))==2}
assert voltage_m=={(0,0),(1,3),(2,1)}
assert voltage_t=={(0,0),(3,0),(3,3)}
# Unimodular over Z/4Z; it maps matching incidence voltages to triangle voltages.
def linear(x):return ((2*x[0]+3*x[1])%4,(x[0]+x[1])%4)
assert {linear(x) for x in voltage_m} == voltage_t
assert len({linear(x) for x in D})==16
phi={tr_m(Mi,x):tr_t(Ti,linear(x)) for Mi,Ti in ((M0,T0),(M1,T1)) for x in D}
assert len(phi)==32 and set(phi)==M and set(phi.values())==T
EX={(a,b) for a,b in combinations(sorted(M,key=lambda z:sorted(z)),2) if len(a&b)==1}
ET={(a,b) for a,b in combinations(sorted(T,key=lambda z:sorted(z)),2) if len(a&b)==2}
assert len(EX)==len(ET)==48
assert {frozenset((phi[a],phi[b])) for a,b in EX} == {frozenset((a,b)) for a,b in ET}
assert all(len(a&b)!=2 for a,b in combinations(M,2))
print('VERIFY_OK: 32 optimum matchings and 32 triangles, two free translation orbits of 16 each')
print('VERIFY_OK: each of 48 original edges is in exactly two optimum matchings')
print('VERIFY_OK: voltage sets mapped by invertible (2x+3y, x+y) over Z4; 48 adjacencies biject')
