#!/usr/bin/env python3
"""Reproducible integer and symbolic checks for the weight-12 toric threefold.
Requires Python 3 and SymPy (version 1.14 tested). This is corroboration;
the mathematical proof is provided in RESULT.md.
"""
from itertools import product
import sympy as sp
v = a,b,c,d,e,f,g = sp.symbols('a b c d e f g')
F = [a*f-b**2, b*e-c**2, b*g-c*d, c*g-d*e]
# Main chart elimination identities.
assert [sp.expand(z.subs({b:d*d*e,c:d*e,g:1})) for z in F] == [a*f-d**4*e**2,0,0,0]
assert [sp.expand(z.subs({b:c*c,d:c*g,e:1})) for z in F] == [a*f-c**4,0,0,0]
assert [sp.expand(z.subs({c:b*g,e:b*g*g,d:1})) for z in F] == [a*f-b**2,0,0,0]
# On a=1 or f=1, the residual equations are the 2x2 minors.
M = sp.Matrix([[b,c,d],[c,e,g]])
minors = [M.extract([0,1],cols).det() for cols in [(0,1),(0,2),(1,2)]]
assert [sp.expand(z.subs({a:1,f:b*b})) for z in F[1:]] == minors
assert [sp.expand(z.subs({f:1,a:b*b})) for z in F[1:]] == minors
# Exhaust all seven-coordinate torus orbit support patterns.
J=sp.Matrix(F).jacobian(v)
# Columns of the paper's exponent matrix, restricted to active generators.
A=sp.Matrix([[6,3,2,1,1,0,0],
             [0,2,1,1,0,4,0],
             [0,0,1,0,2,0,1],
             [0,0,0,1,0,0,1]])
strata=[]
for bits in product((0,1), repeat=7):
    if not any(bits): continue
    vals=dict(zip(v,bits))
    if any(expr.subs(vals) != 0 for expr in F): continue
    supp=tuple(k for k,x in zip('abcdefg',bits) if x)
    inds=[i for i,x in enumerate(bits) if x]
    D=sp.Matrix.hstack(*(A[:,i]-A[:,inds[0]] for i in inds[1:])) if len(inds)>1 else sp.zeros(4,0)
    dim=D.rank()
    rank=J.subs(vals).rank()
    strata.append((supp,dim,rank))
assert len(strata)==21
assert sorted(sum(d==i for _,d,_ in strata) for i in range(4))==sorted([5,9,6,1])
singular={x[0] for x in strata if x[2]<3}
assert singular=={('a',),('f',),('d',),('e',),('g',),('d','g'),('e','g')},singular
# Rank of the smooth torus representative and maximal rank across support list.
assert next(r for supp,dim,r in strata if len(supp)==7)==3
assert all(r==3 for supp,dim,r in strata if supp not in singular)
print('WEIGHT12_CHART_IDENTITIES_OK: 5 charts')
print('TORUS_ORBIT_JACOBIAN_RANKS_OK: 21 supports, 7 singular orbits')
print('SINGULAR_SUPPORTS_OK:',sorted(''.join(t) for t in singular))
print('EXACT_GEOMETRY_REQUIRES_WRITTEN_CHART_PROOF')
