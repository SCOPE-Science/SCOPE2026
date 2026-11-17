"""Exact rational-polynomial verification for the Banach--Mazur deformation theorem.

Each Laurent-free corner inequality is certified on [0,1] by a
Bernstein-form representation with nonnegative rational coefficients.
The three exceptional edge-pair classes are treated analytically in RESULT.md.
Requires sympy; run python checker.py.
"""
from itertools import product
from math import comb
import sympy as sp

T=sp.symbols('t')
U=sp.symbols('u')
C=1+T/2
V=[(sp.Integer(1),sp.Integer(0)),(1,T),(T,1),(0,1),(-1,0),(-1,-T),(-T,-1),(0,-1)]
TABLE=[
[4,4,None,None,6,0,0,0],
[0,0,0,None,6,2,0,0],
[0,0,0,None,None,2,2,0],
[0,0,0,8,None,None,None,10],
[5,0,0,0,7,7,None,None],
[5,1,0,0,1,3,3,None],
[None,1,1,0,1,1,3,None],
[None,None,None,9,1,1,1,11],
]
SPECIAL={(0,2),(0,3),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),
         (4,6),(4,7),(5,7),(6,0),(6,7),(7,0),(7,1),(7,2)}

def determinant(r,s):
    return sp.expand(r[0]*s[1]-r[1]*s[0])

def branches(r,s):
    a,b=r;cc,d=s
    terms=[(d,b),(cc,a),(d-T*cc,b-T*a),(T*d-cc,T*b-a)]
    return [sp.expand(e*x+f*y) for x,y in terms for e,f in product((1,-1),repeat=2)]

def bernstein(P,left,right,degree=8):
    Q=sp.Poly(sp.expand(P.subs(T,left+(right-left)*U)),U)
    assert Q.degree()<=degree
    aa=[Q.nth(k) for k in range(degree+1)]
    return [sum(aa[k]*sp.Rational(comb(i,k),comb(degree,k)) for k in range(i+1))
            for i in range(degree+1)]

checks=0
for i,j in product(range(8),repeat=2):
    branch=TABLE[i][j]
    if branch is None:
        assert (i,j) in SPECIAL
        continue
    assert (i,j) not in SPECIAL
    for ni,nj in product((0,1),repeat=2):
        a=V[(i+ni)%8]; b=V[(j+nj)%8]
        poly=sp.expand(branches(a,b)[branch]-C*determinant(a,b))
        for k in range(8):
            coeffs=bernstein(poly,sp.Rational(k,8),sp.Rational(k+1,8))
            assert all(z>=0 for z in coeffs),(i,j,ni,nj,k,coeffs)
            checks+=len(coeffs)
# Upper bound, in exact symbolic arithmetic.
k=T/(2+T)
assert sp.simplify((1+k)/(1-k*k)-(1+T/2))==0
# The remaining exceptional cells are mapped to three analytic cases.
swap={0:2,1:1,2:0,3:7,4:6,5:5,6:4,7:3}
def orbit(pair):
    seen={pair};pending=[pair]
    while pending:
        i,j=pending.pop()
        for z in [((i+4)%8,j),(i,(j+4)%8),(swap[i],swap[j]),(j,i)]:
            if z not in seen:seen.add(z);pending.append(z)
    return seen
assert SPECIAL <= orbit((0,2))|orbit((0,3))|orbit((1,3))
# The (0,3) gap comparison is concave in u; check its endpoints.
u=sp.symbols('u');f=sp.expand((2*u-1)*(2+2*C*(1-u*T))-T*(2*C*u-1))
assert sp.simplify(sp.diff(f,u,2))==-4*T*(T+2)
assert sp.simplify(f.subs(u,1/C)-8*(1-T)/(T+2))==0
assert sp.simplify(f.subs(u,1)-2*(1-T)*(T+2))==0
print('DEFORMATION_EXACT_BERNSTEIN_OK',checks,'coefficients,',64-len(SPECIAL),'cells')
