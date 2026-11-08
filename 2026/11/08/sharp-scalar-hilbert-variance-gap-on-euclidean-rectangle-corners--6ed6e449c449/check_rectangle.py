#!/usr/bin/env python3
"""Independent finite-vertex checks of sharp four-corner scalar variance bounds.
Uses exact rational coefficients and SymPy quadratic radicals.  The global
mathematical proof is in RESULT.md; this checker corroborates selected cases.
"""
from itertools import combinations
from sympy import Matrix, Rational, sqrt, simplify, sign

CASES=[(1,1),(2,1),(5,2),(3,2),(8,3),(5,4),(7,7),(11,1),(9,8),(4,3)]
M=Matrix([[-1,0,0],[0,-1,0],[0,0,-1],[1,0,1],[0,1,1],[1,1,0]])
count=0
for raw_a,raw_b in CASES:
    x=Rational(max(raw_a,raw_b),2)
    y=Rational(min(raw_a,raw_b),2)
    z=sqrt(x*x+y*y)
    rhs=Matrix([0,0,0,x,y,z]); feasible=[]
    for inds in combinations(range(6),3):
        tri=M[list(inds),:]
        if tri.det()==0:continue
        point=tri.inv()*rhs[list(inds),:]
        if all(sign(simplify((M*point-rhs)[i]))<=0 for i in range(6)):
            val=sum(point[j]**2 for j in range(3))
            feasible.append((val,point))
    assert feasible
    predicted=simplify(x*x+(z-x)**2)
    for val,point in feasible:
        assert sign(simplify(val-predicted))<=0,(raw_a,raw_b,val,predicted)
        count+=1
    assert any(simplify(val-predicted)==0 for val,point in feasible)
    hilbert=x*x+y*y
    gap=simplify(hilbert-predicted)
    assert simplify(gap-2*x*(z-x))==0
    assert gap>0
    if x==y:
        assert simplify(predicted-4*x*x*(1-1/sqrt(2)))==0
print('EXACT_RADICAL_RECTANGLE_VERTEX_COMPARISONS_PASSED',count)
print('SCALAR_HILBERT_GAP_IDENTITIES_PASSED',len(CASES))
print('EXACT_SQUARE_CONSTANT',simplify(Rational(1,4)+(sqrt(2)-1)**2/4))
print('ALL_RECTANGLE_VARIANCE_CHECKS_PASSED')
