"""Exact, stand-alone fourth-moment cubature checks for quadratic spherical-harmonic trace spectra.
This program is for reproducibility of a mathematical statement; no external data or network.
Python 3.9+, standard library only.  Does not certify the general analytic proof.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import isclose, sqrt

checks = 0

def check(statement, context):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(context)

def cubature(n):
    # Degree-four exact weighted cubature on S^(n-1): coordinate axes
    # and the full Rademacher hypercube of norm-one vectors.
    # Each point encoded as integer vector V and squared scale S:
    # physical point = V / sqrt(S), so every quadratic evaluation is rational.
    w_axes = Q(2, n+2) / n
    w_signs = Q(n, n+2) / 2**n
    for i in range(n):
        v = [0]*n
        v[i] = 1
        yield tuple(v), 1, w_axes
    for v in product((-1, 1), repeat=n):
        yield v, n, w_signs

def basis(m):
    # Polynomial is a tuple of coefficient/multi-index monomials.
    # Normalized traces are not assumed. This is an independent full basis.
    n = 2*m
    yield ('Z',[(1,i,i) for i in range(m)] + [(-1,i,i) for i in range(m,n)])
    for off, name in ((0,'X'),(m,'Y')):
        for i in range(m-1):
            yield (name,[(1,off+i,off+i),(-1,off+i+1,off+i+1)])
        for i,j in combinations(range(m),2):
            yield (name,[(1,off+i,off+j)])
    for i in range(m):
        for j in range(m):
            yield ('M',[(1,i,m+j)])

def evaluate(poly, v, scale):
    return sum(Q(a*v[i]*v[j],scale) for a,i,j in poly)

def torus_gram(m, t, b1, b2):
    # Separates mixed monomials, whose cross terms with the even polynomial
    # components vanish by independent sign symmetries.
    tp = list(cubature(m))
    def local(poly, v, scale, start):
        return sum(Q(a*v[i-start]*v[j-start],scale)
                   for a,i,j in poly if start <= i < start+m and start <= j < start+m)
    def means(poly,start):
        return sum(w*local(poly,v,s,start) for v,s,w in tp)
    def prod_mean(poly,qpoly,start):
        return sum(w*local(poly,v,s,start)*local(qpoly,v,s,start) for v,s,w in tp)
    p0, p1 = b1
    q0, q1 = b2
    if p0=='M' and q0=='M':
        # Independent product of first moments of coordinate pairs.
        (a,i,j), = p1
        (b,k,l), = q1
        return Q(a*b)*t*(1-t)*Q(int(i==k)*int(j==l),m*m)
    if p0=='M' or q0=='M':
        return Q(0)
    return (t*t*prod_mean(p1,q1,0) + (1-t)*(1-t)*prod_mean(p1,q1,m)
            +t*(1-t)*(means(p1,0)*means(q1,m) + means(q1,0)*means(p1,m)))

def ambient_gram(n, b1, b2):
    return sum(w*evaluate(b1[1],v,s)*evaluate(b2[1],v,s)
               for v,s,w in cubature(n))

for m in (2,3,4):
    bs = list(basis(m))
    check(len(bs)==2*m*m+m-1, ('basis count',m))
    for t in (Q(1,3), Q(2,5)):
        lam = {'Z':4*(m+1)*(t-Q(1,2))**2,
               'X':Q(4*(m+1),m+2)*t*t,
               'Y':Q(4*(m+1),m+2)*(1-t)**2,
               'M':Q(4*(m+1),m)*t*(1-t)}
        for i, bi in enumerate(bs):
            for bj in bs[i:]:
                a = ambient_gram(2*m,bi,bj)
                z = torus_gram(m,t,bi,bj)
                expected = a*lam[bi[0]] if bi[0]==bj[0] else Q(0)
                check(z==expected, ('Gram',m,t,bi,bj,a,z,expected))
        check(min(lam.values())>0,('injective',m,t))
    at = Q(1,2)
    check(torus_gram(m,at,bs[0],bs[0]) == 0,('balanced kernel',m))
    # Verify eigenvalue ordering and the exact optimizer numerically as an
    # additional independent sanity test (not a substitute for proof).
    s=sqrt(m+2)
    t0=s/(2*(s+1))
    def ls(x):
        return [4*(m+1)*(x-.5)**2,4*(m+1)/(m+2)*x*x,
                4*(m+1)/(m+2)*(1-x)**2,4*(m+1)/m*x*(1-x)]
    lo,hi=min(ls(t0)),max(ls(t0))
    check(isclose(sqrt(hi/lo),1+2/s,rel_tol=1e-13),('optimal kappa',m))
    for x in [j/1000 for j in range(1,1000) if j!=500]:
        z=ls(x)
        check(sqrt(max(z)/min(z)) +1e-11>=1+2/s,('grid sanity',m,x))

print('CLIFFORD_EXACT_CHECKS_PASS',checks)
