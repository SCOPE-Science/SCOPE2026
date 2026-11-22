"""Exact low-order checks for neighboring pure Landau disk spectra.
The all-order assertion follows from the identities proved in RESULT.md.
"""
import math
import sympy as S
from scipy.special import roots_genlaguerre, roots_hermitenorm

x=S.symbols('x', positive=True)
checks=0
for q in range(0,8):
    for k in range(0,13):
        a=S.expand(S.assoc_laguerre(q,k-q,x))
        b=S.expand(S.assoc_laguerre(q,k+1-q,x))
        # The differential identity is equivalent to the exact integrated
        # neighboring-concentration formula after both endpoints vanish.
        lhs=S.diff(S.exp(-x)*x**(k-q+1)*a*b,x)
        rhs=S.exp(-x)*x**(k-q)*((k+1)*a*a-x*b*b)
        assert S.simplify((lhs-rhs)/S.exp(-x))==0,(q,k)
        assert S.expand(S.diff(a,x)-(a-b))==0,(q,k,'contiguous')
        assert S.simplify(x*S.diff(b,x)-((k+1)*a-(k-q+1)*b))==0,(q,k,'ODE')
        checks+=3
        if k<q:
            assert S.simplify(a-(-x)**(q-k)*S.factorial(k)/S.factorial(q)*S.assoc_laguerre(k,q-k,x))==0
            checks+=1
        # Count the positive roots in the *two factors* without asserting
        # an inference from samples to the general theorem.
        if q>0:
            aa=S.Poly(a,x);bb=S.Poly(b,x)
            pa=[r for r in S.polys.polytools.intervals(aa,eps=S.Rational(1,10**9)) if r[0][1]>0]
            pb=[r for r in S.polys.polytools.intervals(bb,eps=S.Rational(1,10**9)) if r[0][1]>0]
            assert len(pa)+len(pb)==(2*q if k>=q else 2*k+1),(q,k,len(pa),len(pb))
            checks+=1
# Verify degree and Hermite root scaling at a fixed large area using
# exact Charlier polynomial coefficients (the proof uses generating functions).
y=S.symbols('y')
for q in range(1,8):
    F=S.expand(sum((-x)**s/S.factorial(s)*S.prod(y-i for i in range(q-s))/S.factorial(q-s) for s in range(q+1)))
    assert S.degree(F,y)==q
    checks+=1
    area=10000
    pol=S.Poly(F.subs(x,area),y)
    roots=S.polys.polytools.intervals(pol,eps=S.Rational(1,10**6))
    real=[float((I[0]+I[1])/2) for I,mult in roots if I[0]>0]
    assert len(real)==q and all(real[i+1]-real[i]>1.0 for i in range(q-1)),(q,real)
    assert all(abs((real[i]-area)/area**.5-float(roots_hermitenorm(q)[0][i]))<.15 for i in range(q))
    checks+=2
print('LANDAU_LAGUERRE_PASS checks='+str(checks))
