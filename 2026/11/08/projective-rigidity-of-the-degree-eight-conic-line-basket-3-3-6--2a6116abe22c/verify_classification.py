#!/usr/bin/env python3
"""Exact finite combinatorics and normal-form elimination for the rigidity theorem."""
from itertools import combinations
import sympy as sp
# 6 distinct lines: a line-only ordinary triple uses three of the 15 line pairs.
L=range(6); pairs=set(combinations(L,2)); triples=list(combinations(L,3))
def edges(t):return set(combinations(t,2))
quadruples=[]
for tri in combinations(triples,4):
    touched=set()
    for t in tri:
        e=edges(t)
        if touched&e:break
        touched|=e
    else:
        left=pairs-touched
        # Every 4-triple line arrangement is a complete quadrangle: three residual
        # line pairs have pairwise disjoint sets of participating lines.
        assert len(left)==3
        assert len(set(sum((list(p) for p in left),[])))==6, (tri,left)
        quadruples.append((tri,left))
assert len(quadruples)>0
# A line tangent to a smooth conic cannot participate in a conic-containing
# ordinary triple. Two of three residual nodes consume four distinct lines,
# leaving at most two lines eligible as tangents, not the required three.
for tri,left in quadruples:
    for two in combinations(left,2):
        assert len({i for p in two for i in p})==4
# The coordinate-normal-form conditions on three distinct tangent lines.
s,t,u=sp.symbols('s t u');
# Pairwise intersections on x=0, y=0, z=0, respectively.
Ex=sp.factor(((s+1)**2*t**2-(t+1)**2*s**2)/(s-t))
Ey=sp.factor((u**2-s**2)/(u-s))
Ez=sp.factor(((t+1)**2-(u+1)**2)/(t-u))
assert sp.expand(Ex)==-2*s*t-s-t
assert sp.expand(Ey)==u+s
assert sp.expand(Ez)==t+u+2
# Ey=0 => u=-s; Ez=0 => t=s-2; then Ex=0 => s^2-s-1=0.
assert sp.simplify(Ex.subs({t:s-2})+2*(s*s-s-1))==0
R=sp.Symbol('R'); M=R**2-R-1
def rd(e):return sp.rem(sp.Poly(sp.expand(e),R),sp.Poly(M,R)).as_expr()
# The involution [x:y:z] -> [z:y:x] sends tangent parameter z to 1/z,
# exchanging the two roots and therefore the two labelled solutions.
assert rd(R*(R-1)-1)==0
assert rd((R-2)*(-R-1)-1)==0
# Other root is 1-R; compare tangent parameter sets after inversion.
A=[R,R-2,-R];other=[1-R,-1-R,R-1]
for x,y in zip(A,[R-1,-1-R,1-R]):
    assert rd(x*y-1)==0
assert set(map(str,other))==set(map(str,[1-R,(1-R)-2,-(1-R)]))
print('PASS: all 4-triple line patterns have three disjoint residual pairs; normal form has two conjugate roots in one projective orbit.')
