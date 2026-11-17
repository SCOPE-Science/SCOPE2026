"""Finite exact arithmetic diagnostics for a polynomial-reset hybrid oscillator.

Does not certify the all-degree theorem, whose proof is analytic.
"""
import sympy as sp
from sympy import Poly

u=sp.symbols('u')

def cheb_reset(n,delta=sp.Rational(1,2)):
    return sp.expand(sp.Rational(1,2)+(1+delta)*(-1)**(n+1)*sp.chebyshevt(n,2*u-1)/2)

def iterate(f,m):
    g=u
    for _ in range(m):
        g=sp.Poly(f,u).compose(sp.Poly(g,u)).as_expr()
    return sp.Poly(g-u,u)

for n,k in ((2,1),(2,2),(3,1)):
    f=cheb_reset(n)
    P=iterate(f,2*k)
    roots=P.count_roots(0,1)
    assert roots==n**(2*k), (n,k,roots,n**(2*k))
    assert sp.gcd(P,P.diff()).degree()==0
    assert sp.Poly(P,u).degree()==n**(2*k)
    print('degree',n,'return_iterate',k,'real_simple_roots_0_1',roots,flush=True)
for n in range(2,9):
    f=cheb_reset(n)
    assert f.subs(u,0)<0
    # Interior extrema should alternate and lie strictly outside [0,1].
    for j in range(1,n):
        xj=(1+sp.cos(sp.pi*j/n))/2
        fj=sp.simplify(f.subs(u,xj))
        assert min(abs(float(sp.N(fj-sp.Rational(-1,4),35))), abs(float(sp.N(fj-sp.Rational(5,4),35)))) < 1e-24, (n,j,fj)
print('CHEBYSHEV_HYBRID_SHARP_CYCLE_COUNT_CHECK_OK')
