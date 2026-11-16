#!/usr/bin/env python3
"""Reproducible exact and finite numerical checks of the stated spectral identities.
Not a substitute for the general proof."""
import sympy as s
import mpmath as mp
import math
assertions = 0
def check(condition):
    global assertions
    assert bool(condition)
    assertions += 1
x=s.symbols('x')
for n in range(1,17):
    poly=s.Poly(s.legendre(n,1-2*x),x)
    # Integral of (log x)/2 times shifted Legendre polynomial.
    val=s.Rational(1,2)*sum(coeff*s.Rational(-1,(deg[0]+1)**2) for deg,coeff in poly.terms())
    check(s.simplify(val+s.Rational(1,2*n*(n+1)))==0)
for n in range(1,17):
    poly=s.Poly(s.legendre(n,1-2*x),x)
    value=sum(coeff*s.Rational(1,deg[0]+1) for deg,coeff in poly.terms())
    check(value==0)
kvals={3:(1-s.zeta(3))/4,4:s.Rational(5,16)-s.zeta(3)/4,5:(7-5*s.zeta(3)-s.zeta(5))/16}
for k,formula in kvals.items():
    l=s.symbols('l',integer=True,positive=True)
    exact=s.summation((2*l+1)*(-(s.Rational(1,2)/(l*(l+1))))**k,(l,1,s.oo))
    check(s.simplify(exact-formula)==0)
    mp.mp.dps=60
    target=mp.mpf(str(s.N(formula,52)))
    approx=mp.fsum((2*l+1)*(-mp.mpf(1)/(2*l*(l+1)))**k for l in range(1,250))
    check(abs(target-approx)<mp.mpf('1e-6'))
for k in range(3,21):
    terms=[(2*l+1)*(-mp.mpf(1)/(2*l*(l+1)))**k for l in range(1,200)]
    check(mp.sign(mp.fsum(terms))==(-1)**k)
    # Geometric gap: all other modes have smaller absolute eigenvalue.
    check(abs(mp.fsum(terms[1:])) <= mp.mpf(10)*(mp.mpf(1)/12)**k)
for j in range(2,19):
    # Exact exponential-law cumulant for X=(1+log U)/2.
    t=s.symbols('t')
    cg=s.Rational(1,2)*t-s.log(1+t/2)
    check(s.diff(cg,t,j).subs(t,0)==(-1)**j*s.factorial(j-1)/2**j)
print(f'PASS: {assertions} exact/spectral assertions; finite tests do not prove the theorem')
