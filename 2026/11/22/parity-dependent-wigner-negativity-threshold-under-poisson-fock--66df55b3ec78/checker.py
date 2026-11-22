"""Standalone exact-arithmetic checks for a lossy oscillator with Poisson Fock re-preparation.
Run: python checker.py (requires sympy). Checks finite certificates, not a proof for all n.
"""
from fractions import Fraction
from math import comb
import sympy as S

a,z = S.symbols('a z', positive=True)
checks=0

def eq(x,y):
    global checks
    assert S.cancel(x-y) == 0, (x,y)
    checks+=1

def pk(n,k,rate):
    return S.factor(rate * S.factorial(n) * S.rf(rate,k) /
                    (S.factorial(k)*S.rf(rate,n+1)))

for n in range(1,10):
    p=[pk(n,k,a) for k in range(n+1)]
    eq(sum(p),1)
    for k in range(n+1):
        eq((k+1)*(p[k+1] if k<n else 0)-k*p[k]-a*p[k]+(a if k==n else 0),0)
        eq(p[k].subs(a,1),S.Rational(1,n+1))
        if k<n: eq(p[k+1]/p[k],(a+k)/(k+1))
    poly=S.factor(sum(p[k]*(-1)**k*S.laguerre(k,z) for k in range(n+1)))
    eq(poly.subs(z,0),S.factor(a*S.integrate((1-2*S.Symbol('t'))**n*S.Symbol('t')**(a-1),(S.Symbol('t'),0,1))))
    for rate in (S.Rational(1,3),S.Rational(2,3),S.Integer(1),S.Rational(3,2),S.Integer(3)):
        values=[p[k].subs(a,rate) for k in range(n+1)]
        eq(sum(values),1)
        for k in range(n+1):
            eq((k+1)*(values[k+1] if k<n else 0)-k*values[k]-rate*values[k]+(rate if k==n else 0),0)
        # The Laguerre-weighted Wigner polynomial has the expected leading coefficient.
        eq(S.Poly(poly.subs(a,rate),z).LC(),values[-1]/S.factorial(n))
    # At the uniform rate, a known Wigner-positive balanced-beamsplitter mixture.
    uniform_poly=sum((-1)**k*S.laguerre(k,z) for k in range(n+1))/S.Integer(n+1)
    eq(poly.subs(a,1), uniform_poly)
    binomial_half_poly=sum(S.binomial(n,k)*(-1)**k*S.laguerre(k,z)/2**n for k in range(n+1))
    eq(binomial_half_poly,(z/2)**n/S.factorial(n))

p2=S.factor(sum(pk(2,k,a)*(-1)**k*S.laguerre(k,z) for k in range(3)))
expected=(a*a-a+2-2*a*a*z+a*(a+1)*z*z/S.Integer(2))/((a+1)*(a+2))
eq(p2,expected)
zstar=2*a/(a+1)
eq(S.diff(p2,z).subs(z,zstar),0)
eq(p2.subs(z,zstar),(-a**3+a+2)/((a+1)**2*(a+2)))
# Strict majorization of the vector p(rate) away from uniform, exact for sample rates.
for n in range(1,10):
    for low,high in ((S.Rational(1,4),S.Rational(3,4)), (S.Rational(5,4),S.Rational(7,4))):
        l=[pk(n,k,low) for k in range(n+1)];h=[pk(n,k,high) for k in range(n+1)]
        l.sort(reverse=True); h.sort(reverse=True)
        for j in range(1,n+1):
            assert (sum(l[:j])>sum(h[:j])) if high<1 else (sum(h[:j])>sum(l[:j]))
            checks+=1

print('PASS:',checks,'symbolic identity and rational-inequality checks')
