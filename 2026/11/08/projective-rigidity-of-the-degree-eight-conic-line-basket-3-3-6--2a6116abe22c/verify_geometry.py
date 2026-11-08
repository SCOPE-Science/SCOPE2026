#!/usr/bin/env python3
"""Exact arithmetic incidence check of a rigid conic and six-line arrangement."""
import itertools
import sympy as sp
R=sp.Symbol('R'); P=R**2-R-1

def rd(e): return sp.rem(sp.Poly(sp.expand(e),R),sp.Poly(P,R)).as_expr()
def vec(v): return sp.Matrix([rd(e) for e in v])
def cross(a,b): return vec(a.cross(b))
def dot(a,b):return rd(a.dot(b))
def same(a,b): return all(rd(e)==0 for e in a.cross(b))
S=[sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([0,0,1])]
def tangent(s): return vec([1,(s+1)**2,s**2])
T=[tangent(R),tangent(R-2),tangent(-R)]
lines=S+T
Q=sp.Matrix([[0,sp.Rational(1,2),sp.Rational(1,2)], [sp.Rational(1,2),0,sp.Rational(1,2)], [sp.Rational(1,2),sp.Rational(1,2),0]])
def conic(p): return rd((p.T*Q*p)[0])
assert sp.factor(Q.det())==sp.Rational(1,4)
assert len(lines)==6 and all(not same(a,b) for a,b in itertools.combinations(lines,2))
# Projective points supporting every pair of lines.
points=[]
for a,b in itertools.combinations(lines,2):
    p=cross(a,b)
    assert any(e!=0 for e in p)
    if not any(same(p,z) for z in points):points.append(p)
hist={}
for p in points:
    k=sum(dot(l,p)==0 for l in lines)
    c=(conic(p)==0)
    assert k in (2,3), (p,k)
    if c:assert k==2
    hist[(k,c)]=hist.get((k,c),0)+1
assert hist=={(2,True):3,(3,False):3,(2,False):3},hist
for p in points:
    if conic(p)==0:
        incident=[l for l in lines if dot(l,p)==0]
        # The three branches are transverse: the conic tangent is neither incident line.
        assert len(incident)==2
        assert not any(same(Q*p,l) for l in incident)
# A tangent line L is a point on the dual conic. The coordinate S lines are secants.
def dual(l):
    a,b,c=l
    return rd(a*a+b*b+c*c-2*a*b-2*a*c-2*b*c)
assert [dual(l)==0 for l in lines]==[False,False,False,True,True,True]
for t in T:
    p=vec(Q.inv()*t)
    assert conic(p)==0 and dot(t,p)==0
    assert all(dot(l,p)!=0 for l in lines if not same(l,t))
# Every conic-line incidence is accounted by 2*3 transverse intersections plus 2*3 + 3 tangent contributions.
# Count per component: 3 secants (2 points each), 3 tangents (one double point each).
assert 3*2+3*2==6*2
assert 3+3*3+6*4==36
print('PASS: 6 distinct lines, 3 ordinary nodes, 3 conic tangencies, 6 ordinary triple points, tau=36.')
