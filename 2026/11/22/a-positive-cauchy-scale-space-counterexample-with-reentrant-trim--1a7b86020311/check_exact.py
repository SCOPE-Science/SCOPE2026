#!/usr/bin/env python3
"""Exact algebraic certificate for four Cauchy/Poisson scale-space mode counts.
Requires sympy (tested with 1.13+). No floating-point input or approximations.
"""
import sympy as s
x,y,q=s.symbols('x y q',real=True)
w=s.Rational(49,100)
H=w/(x*x+q)+1/((x-1)**2+q)+1/((x+1)**2+q)
D=(x*x+q)**2*((x-1)**2+q)**2*((x+1)**2+q)**2
P=(w+2)*y**4 +4*(q*w+2*q-w+1)*y**3 \
 +2*(3*q*q*w+6*q*q-2*q*w+2*q+3*w-3)*y**2 \
 +4*(q+1)*(q*q*w+2*q*q-3*q-w)*y \
 +(q+1)*(q**3*w+2*q**3+3*q*q*w-6*q*q+3*q*w+w)
assert s.cancel(s.diff(H,x)+2*x*P.subs(y,x*x)/D)==0
cases=[
(s.Rational(1,2),[1328,3744,904,-4376,323],[(0,1),(s.Rational(1,10),-1),(1,1)],3),
(s.Integer(1),[249,1200,1392,-800,-16],[(0,-1),(1,1)],2),
(s.Rational(6,5),[155625,874500,1306350,-277420,4609],[(0,1),(s.Rational(1,20),-1),(s.Rational(1,5),1)],3),
(s.Rational(3,2),[3984,27168,53784,9800,3625],[(0,1),(1,1)],1)
]
for Q,coeff,signs,modes in cases:
    poly=s.Poly(P.subs(q,Q),y)
    prim=poly.clear_denoms()[1].primitive()[1]
    assert prim.all_coeffs()==coeff,(Q,prim.all_coeffs())
    signs_desc=[s.sign(c) for c in coeff if c]
    variations=sum(signs_desc[i]!=signs_desc[i+1] for i in range(len(signs_desc)-1))
    for v,expected in signs:
        got=s.sign(poly.eval(v)); assert got==expected,(Q,v,got,expected)
    expected_positive={s.Rational(1,2):2,s.Integer(1):1,s.Rational(6,5):2,s.Rational(3,2):0}[Q]
    assert variations==expected_positive,(Q,variations,expected_positive)
    # For 1/2 and 6/5, two disjoint strict sign brackets force two positive roots;
    # for 1, opposite endpoint signs force one; for 3/2, all coefficients are positive.
    assert (modes==2 if poly.eval(0)<0 else (modes==1 if variations==0 else modes==3))
    print(f'q={Q}: Descartes upper bound {variations}, exact positive-root count {expected_positive}, strict modes {modes}')
print('PASS: exact rational coefficient, factorization, sign, and mode-count certificate')
