"""Reproducibility checks for the hypercube one-shortcut spectral theorem.
Run with Python 3, NumPy, and SymPy. All symbolic checks use exact rationals.
"""
from fractions import Fraction
from math import comb
import numpy as np
import sympy as sp


def laplacian(d):
    n = 1 << d
    L = [[0] * n for _ in range(n)]
    for x in range(n):
        L[x][x] = d
        for j in range(d):
            L[x][x ^ (1 << j)] = -1
    return L


def spectral_mass(d, r, k):
    odd_count = sum(comb(r, j) * comb(d-r, k-j)
                    for j in range(1, r+1, 2) if 0 <= k-j <= d-r)
    return Fraction(4 * odd_count, 1 << d)


def resonance(d, r):
    assert r % 2 == 0 and 2 <= r < d
    return 1 / sum((spectral_mass(d, r, k) / (2*(d-k))
                    for k in range(1, d)), Fraction(0))


def independent_mass(d, r, k):
    u = (1 << r) - 1
    n = 1 << d
    return Fraction(sum((((-1)**((x & u).bit_count())) - 1)**2
                        for x in range(n) if x.bit_count() == k), n)


def count_distinct(vals, atol=4e-7):
    groups = []
    for z in vals:
        if not groups or abs(z-groups[-1]) > atol:
            groups.append(float(z))
    return len(groups)


def run():
    checks = 0
    for d in range(3, 9):
        for r in range(2, d):
            masses = [spectral_mass(d,r,k) for k in range(d+1)]
            assert masses[0] == 0
            assert all(masses[k] > 0 for k in range(1,d))
            assert (masses[d] > 0) == (r % 2 == 1)
            assert sum(masses) == 2
            for k in range(d+1):
                assert masses[k] == independent_mass(d,r,k)
                checks += 1
            n=1<<d
            L=np.array(laplacian(d),dtype=float)
            b=np.zeros(n); b[0]=1; b[(1<<r)-1]=-1
            ts = [Fraction(1,3),Fraction(13,10)]
            tstar = resonance(d,r) if r%2==0 else None
            if tstar is not None:
                ts = [tstar/3,tstar,2*tstar]
            for t in ts:
                ev=np.linalg.eigvalsh(L+float(t)*np.outer(b,b))
                expected=2*d-(int(t==tstar) if tstar is not None else 0)
                got=count_distinct(ev)
                assert got==expected,(d,r,t,got,expected)
                checks+=1
                # Every original interior eigenvalue survives with positive multiplicity.
                for k in range(1,d):
                    assert min(abs(ev-2*k))<3e-8,(d,r,k)
                    checks += 1
    for d in range(3, 30):
        assert resonance(d,2) == Fraction((d-1)*(1 << (d-2)), (1 << (d-1))-1)
        checks+=1
    # Exact full-matrix nullity tests at the first two dimensions.
    for d in range(3,5):
        for r in range(2,d):
            L=sp.Matrix(laplacian(d))
            b=sp.zeros(1<<d,1);b[0]=1;b[(1<<r)-1]=-1
            if r%2==0:
                t=resonance(d,r)
                A=L+sp.Rational(t.numerator,t.denominator)*b*b.T
                null=(1<<d)-(2*d*sp.eye(1<<d)-A).rank()
                assert null==2,(d,r,null)
            else:
                A=L+sp.Rational(4,3)*b*b.T
                null=(1<<d)-(2*d*sp.eye(1<<d)-A).rank()
                assert null==0,(d,r,null)
            checks += 1
    print(f'PASS: {checks} spectral masses, eigenvalue and exact-rank assertions')

if __name__=='__main__':
    run()
