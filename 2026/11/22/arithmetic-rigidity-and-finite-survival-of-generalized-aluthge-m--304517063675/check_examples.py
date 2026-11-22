"""Exact finite diagnostics for generalized Aluthge transforms of polynomial shifts.

The analytic theorem is proved separately; finite checks below are not an infinite proof.
"""
from fractions import Fraction
from math import comb
import sympy as sp

x=sp.Symbol('x')

def candidate_moments(P, t, k, n):
    """Exact positive moments when exponentiation is rational or a square root."""
    t=sp.Rational(t)
    product=sp.Integer(1)
    for j in range(k+1):
        c=sp.Rational(comb(k,j))* (1-t)**(k-j)*t**j
        product *= (P.subs(x,n+j)/P.subs(x,j))**c
    return sp.simplify(sp.powdenest(product, force=True))

def candidate_poly(Q, u, v, k):
    b=[comb(k,j)*(v-u)**(k-j)*u**j for j in range(k+1)]
    R=sp.prod(Q.subs(x,x+j)**b[j] for j in range(k+1))
    return sp.cancel(R/R.subs(x,0))

checks=0
for u,v,k,r in [(1,2,1,2),(1,2,2,4),(1,3,1,3),(2,3,2,9),(2,5,2,25),(1,2,3,8)]:
    Q=x+2
    P=(Q/Q.subs(x,0))**r
    R=candidate_poly(Q,u,v,k)
    assert sp.degree(R,x)==r
    for n in range(13):
        assert sp.simplify(candidate_moments(P,sp.Rational(u,v),k,n)-R.subs(x,n))==0
        checks+=1
    # The smallest finite-difference degree is the degree of the original moment polynomial.
    for n in range(5):
        assert sp.simplify(sum((-1)**(r+1-j)*comb(r+1,j)*R.subs(x,n+j) for j in range(r+2)))==0
        checks+=1

# Even-denominator sign changes make a formally perfect power insufficient.
P=(2*x-1)**2
for n in range(1,10):
    assert candidate_moments(P,sp.Rational(1,2),1,n)==(2*n-1)*(2*n+1)
    checks+=1
assert candidate_moments(P,sp.Rational(1,2),1,0)==1
assert (2*0-1)*(2*0+1)==-1
checks+=2

# Root multiplicities of each coefficient of the r-th power-shift filter force
# divisibility by v**r, checked on several short finite root configurations.
for v,u,k in [(2,1,1),(2,1,2),(3,1,2),(5,2,3)]:
    coefficients=[comb(k,j)*(v-u)**(k-j)*u**j for j in range(k+1)]
    for m in range(1,7):
        for h in range(3):
            roots=[0]*(h+1)
            roots[h]=m
            exps=[sum(coefficients[j]* (roots[i+j] if i+j<len(roots) else 0)
                      for j in range(k+1)) for i in range(len(roots))]
            assert (all(z%(v**k)==0 for z in exps)) == (m%(v**k)==0)
            checks+=1
print(f'EXACT_CHECKS_OK {checks}')
