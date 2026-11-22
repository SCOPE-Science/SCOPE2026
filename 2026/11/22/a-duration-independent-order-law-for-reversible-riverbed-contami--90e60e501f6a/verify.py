#!/usr/bin/env python3
"""Independent finite checks for a two-regime reversible riverbed-storage theorem.

Run: python3 verify.py. Standard library only. The proof is analytical in RESULT.md.
"""
from fractions import Fraction as F
from random import Random
from math import exp, sinh, sqrt, isclose


def prod(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def sub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(2)) for i in range(2))


def scale(a, x):
    return tuple(tuple(x * a[i][j] for j in range(2)) for i in range(2))


def qmat(u, k, r):
    return ((-u-k, r), (k, -r))


def expseries(q, t):
    # Numerical matrix exponential from its defining power series; no spectral formula.
    # Use scaling and squaring for stable rounding at large rates/times.
    norm = max(sum(abs(x) for x in row) for row in q) * t
    squarings = max(0, int(norm) + 1)
    # cap to avoid unnecessarily large work; all test durations/rates are bounded.
    step = t / (2 ** squarings)
    eye = ((1., 0.), (0., 1.))
    out = eye
    term = eye
    for j in range(1, 140):
        term = scale(prod(term, q), step / j)
        out = add(out, term)
        if max(abs(v) for row in term for v in row) < 2e-17:
            break
    for _ in range(squarings):
        out = prod(out, out)
    return out


def mass_after(a, b, z):
    v = (z[0], z[1])
    w = tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
    w = tuple(sum(b[i][j]*w[j] for j in range(2)) for i in range(2))
    return sum(w)


def pref(u, k, r, t):
    d = sqrt((u+k-r)**2 + 4*k*r)
    return 2*exp(-(u+k+r)*t/2)*sinh(d*t/2)/d


def main():
    rng = Random(121092)
    assertions = 0
    # Exact rational commutator and all sign coefficients, separately checked
    # against direct matrix multiplication.
    for _ in range(900):
        vals = [F(rng.randint(1, 18), rng.randint(1, 15)) for j in range(6)]
        uA,kA,rA,uB,kB,rB = vals
        A, B = qmat(uA,kA,rA),qmat(uB,kB,rB)
        C = sub(prod(A,B),prod(B,A))
        alpha = uA*kB-uB*kA
        beta = uB*rA-uA*rB
        assert C[0][0]+C[1][0] == alpha
        assert C[0][1]+C[1][1] == beta
        assertions += 2
        # All nonzero initial compositions, not merely pure starting states.
        x,y = F(rng.randrange(6), 9),F(rng.randrange(6), 9)
        assert sum(C[i][0]*x+C[i][1]*y for i in range(2)) == alpha*x+beta*y
        assertions += 1
    # Taylor-series exponential calculation independent of the hyperbolic formula.
    for _ in range(240):
        uA,kA,rA,uB,kB,rB = [rng.uniform(.2, 3.0) for j in range(6)]
        tA, tB = rng.uniform(.02, 1.7),rng.uniform(.02, 1.7)
        x,y = rng.random(),rng.random()
        A,B=qmat(uA,kA,rA),qmat(uB,kB,rB)
        EA,EB=expseries(A,tA),expseries(B,tB)
        eAB = x+y-mass_after(EA,EB,(x,y))
        eBA = x+y-mass_after(EB,EA,(x,y))
        target = pref(uA,kA,rA,tA)*pref(uB,kB,rB,tB)*(
            (uA*kB-uB*kA)*x+(uB*rA-uA*rB)*y)
        assert isclose(eAB-eBA,target,abs_tol=7e-10,rel_tol=2e-8),(
           eAB-eBA,target)
        assert pref(uA,kA,rA,tA)>0 and pref(uB,kB,rB,tB)>0
        assertions += 3
    # Exact nontrivial all-duration reversal boundary with both rates increasing.
    uA,kA,rA,uB,kB,rB = 1,1,1,3,2,2
    alpha = uA*kB-uB*kA
    beta = uB*rA-uA*rB
    assert (alpha,beta)==(-1,1)
    for x,y in [(2,0),(0,2),(1,1),(4,1),(1,4)]:
        for ta,tb in [(0.2,0.4),(0.8,1.3),(1.7,0.3)]:
            EA,EB=expseries(qmat(uA,kA,rA),ta),expseries(qmat(uB,kB,rB),tb)
            diff = (x+y-mass_after(EA,EB,(x,y)))-(
                    x+y-mass_after(EB,EA,(x,y)))
            expected=alpha*x+beta*y
            assert (diff>1e-12)-(diff< -1e-12)==(expected>0)-(expected<0)
            assertions += 1
    print('VERIFY_OK assertions='+str(assertions))

if __name__=='__main__':
    main()
