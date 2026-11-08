"""Exact finite checks for the vertex-uniform inertia of isocanted cubes.

Run: python3 verify.py. Uses only the Python standard library.
This is corroboration of, not a substitute for, the all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product
from decimal import Decimal, getcontext


def vertices(d, ell, a):
    assert d >= 2 and ell > a > 0
    out = []
    for mask in range(1, 1 << d):
        v = tuple(ell / 2 if mask & (1 << i) else a - ell / 2
                  for i in range(d))
        out.extend((v, tuple(-z for z in v)))
    assert len(out) == (1 << (d + 1)) - 2
    assert len(set(out)) == len(out)
    for v in out:
        assert all(abs(v[i]) <= ell / 2 for i in range(d))
        assert all(abs(v[i]-v[j]) <= ell-a for i in range(d) for j in range(i))
    return out


def theoretical(d, ell, a):
    n = (1 << d) - 1
    r = a / ell
    transverse = F(1 << (d-2), n) * (ell-a)**2
    off = ell**2 * ((1 << d)-4)*r*r / (4*n) + ell**2 * (4*r-1) / (4*n)
    axial = transverse + d * off
    return transverse, axial, off


def check():
    profiles = 0
    vertices_seen = 0
    for d in range(2, 9):
        for a in [F(1, 8), F(1, 4), F(1, 3), F(1, 2), F(3, 4)]:
            ell = F(1)
            vs = vertices(d, ell, a)
            vertices_seen += len(vs)
            profiles += 1
            n = len(vs)
            assert all(sum(v[i] for v in vs) == 0 for i in range(d))
            diag = sum(v[0]*v[0] for v in vs) / n
            offdiag = sum(v[0]*v[1] for v in vs) / n
            for i in range(d):
                assert sum(v[i]*v[i] for v in vs)/n == diag
                for j in range(i):
                    assert sum(v[i]*v[j] for v in vs)/n == offdiag
            lperp, laxial, off = theoretical(d, ell, a)
            assert offdiag == off
            assert diag-offdiag == lperp
            assert diag+(d-1)*offdiag == laxial
            assert laxial > 0 and lperp > 0
            x = a/(ell-a)
            R = 1 + F(d, 1 << d)*(((1 << d)-1)*x*x+2*x-1)
            assert R == laxial/lperp
            # The centered vertex radii are pairwise distinct for all layers.
            radii = [F(k, 4)*ell*ell + (d-k)*(ell/2-a)**2
                     for k in range(1, d+1)]
            assert all(radii[i] < radii[i+1] for i in range(d-1))
    # Even dimensions give rational exact isotropy parameters.
    for d in [2, 4, 6, 8, 10, 12]:
        a = F(1, 2+(1 << (d//2)))
        p, q, off = theoretical(d, F(1), a)
        assert off == 0 and p == q > 0
    # Odd dimensions have quadratic-irrational isotropy parameters.
    getcontext().prec = 70
    for d in [3, 5, 7, 9, 11]:
        s = Decimal(2)**(d//2)*Decimal(2).sqrt()
        a = 1/(Decimal(2)+s)
        q = (Decimal((1 << d)-4)*a*a + 4*a-1)
        assert abs(q) < Decimal('1e-60')
    print('ISOCANTED_VERTEX_INERTIA_CHECKS_PASSED',
          'exact_profiles=', profiles, 'vertices_processed=', vertices_seen,
          'exact_even_isotropy=', 6, 'odd_precision_checks=', 5)


if __name__ == '__main__':
    check()
