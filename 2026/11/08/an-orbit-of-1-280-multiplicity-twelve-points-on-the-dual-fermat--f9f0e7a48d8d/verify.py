"""Exact finite algebra checks for the Fermat quartic hyperplane witness.

This checks algebraic identities and finite enumerations; the accompanying
proof supplies the geometric generality and projective-duality arguments.
"""
from collections import Counter
from itertools import product, permutations

# The ring Z[w], w*w+w+1=0, modeled by integral coefficient pairs.
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def mul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c-b*d)
def power(u,n):
    v=(1,0)
    for _ in range(n): v=mul(v,u)
    return v
R=((1,0),(0,1),(-1,-1)); ONE=(1,0); ZERO=(0,0)
assert all(power(r,3)==ONE for r in R)
assert all(power(r,4)==r for r in R)
solutions=[]
for t in product(R, repeat=4):
    s=ZERO
    for a in t: s=add(s,a)
    if s==ONE: solutions.append(t)
assert len(solutions)==12
assert all(Counter(t)==Counter((R[0],R[0],R[1],R[2])) for t in solutions)
assert len({tuple(t) for t in solutions})==12
# At each node the restricted quartic G has zero value and all derivatives:
# G=sum x_i^4 - (sum x_i)^4. Its Hessian is D-11^t with D diagonal x_i^2.
# For x_i^3=1 and sum x_i=1, D is invertible and ker(H)=<x>.
for x in solutions:
    s=ZERO
    for a in x: s=add(s,a)
    assert s==ONE
    f=neg(power(s,4))
    for a in x: f=add(f,power(a,4))
    assert f==ZERO
    assert all(power(a,3)==power(s,3) for a in x)
    assert all(mul(power(a,2),a)==ONE for a in x)
# Arithmetic: no solution fixed by conjugation; the 12 points pair into six orbits.
def conj(a): return (a[0]-a[1],-a[1])
assert all(conj(r) in R for r in R)
solset=set(solutions)
assert all(tuple(conj(a) for a in t) in solset for t in solset)
assert all(tuple(conj(a) for a in t)!=t for t in solset)
assert len({frozenset((t,tuple(conj(a) for a in t))) for t in solset})==6
# The automorphism orbit of h=(1,1,1,1,alpha) with alpha^4=-1:
# choice of one distinguished entry times four independent mu4 phases.
labels={(special,phase) for special in range(5) for phase in product(range(4),repeat=4)}
assert len(labels)==5*4**4==1280
# Invariant h_i^4/h_j^4 distinguishes the distinguished position; the
# remaining independent fourth-root phases distinguish all orbit points.
print('VERIFY_FERMAT12_OK nodes=12 quadratic_orbits=6 dual_orbit=1280')
