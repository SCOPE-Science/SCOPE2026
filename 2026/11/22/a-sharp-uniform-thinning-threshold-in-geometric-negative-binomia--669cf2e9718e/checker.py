"""Exact arithmetic checks for an Erlang-three/geometric Poisson mixture.

Checks finite identities and a negative coefficient witness; the infinite
quantifiers are proved analytically in RESULT.md and not by this script.
"""
from fractions import Fraction as Q
from math import comb


def complex_mul(u, v):
    return (u[0] * v[0] - u[1] * v[1],
            u[0] * v[1] + u[1] * v[0])


def formal_canonical(p, q, top):
    """Compute coefficients of G'(z)/G(z) by exact formal division."""
    e = 1 - q
    g = [q**n * (p * e + (1-p)*e**3 * comb(n+2, 2))
         for n in range(top+2)]
    assert g[0] > 0
    b = []
    for n in range(top+1):
        b.append(((n+1)*g[n+1] - sum(g[j]*b[n-j] for j in range(1,n+1))) / g[0])
    return b


def complex_canonical(p, q, top):
    """For (1-p)/p=4, use exact Gaussian rationals."""
    assert (1-p)/p == 4
    eps=1-q
    denominator=1+4*eps**2
    w=(q/denominator, -2*q*eps/denominator)
    wn=(Q(1),Q(0))
    b=[]
    for n in range(1,top+2):
        wn=complex_mul(wn,w)
        b.append(3*q**n-2*wn[0])
    return b


def check():
    p,q=Q(1,5),Q(99,100)
    a=formal_canonical(p,q,30)
    b=complex_canonical(p,q,30)
    assert a==b, "Formal power-series differentiation disagrees with root factorization"
    assert all(x>0 for x in b), "Finite positive compound-Poisson coefficients check failed"
    d=[b[i-1]-b[i] for i in range(1,30)]
    assert all(x>0 for x in d[:12]), "First 12 differences were expected positive"
    assert d[12] < 0, "The 13th canonical difference is expected negative"
    assert Q(0)<p<Q(4,9) and Q(0)<q<Q(1)
    assert Q(4,9)/(1-Q(4,9))==Q(4,5)
    print('Independent formal division and Gaussian-rational root coefficients agree through index 31.')
    print('The first 12 canonical differences are positive; the 13th is negative.')
    print('Exact 13th difference numerator:',d[12].numerator)
    print('Exact 13th difference denominator:',d[12].denominator)
    print('Normalized 13th difference approximation:',float(d[12]/q**13))
    print('All finite exact-rational checks passed. Infinite statements need the analytic proof.')

if __name__=='__main__':
    check()
