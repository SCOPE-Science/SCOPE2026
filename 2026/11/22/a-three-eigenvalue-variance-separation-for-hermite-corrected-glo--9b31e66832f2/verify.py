#!/usr/bin/env python3
"""Exact-rational checks for inverse-trace polynomial correction on sparse SPD matrices.

Run: python3 verify.py
All finite tests use fractions; asymptotic assertions in the accompanying proof
follow from displayed rational expressions, not numerical extrapolation.
"""
from fractions import Fraction as Q
from math import comb


def construction(N):
    assert isinstance(N, int) and N >= 2
    q = N**3
    n = q + 2
    mu = Q(q + 3*N, n)
    T = Q(q) + Q(3, 2*N)
    G = Q(n, 1)/mu
    bdiag = Q(3*N, 2)
    boff = -Q(N, 2)
    invdiag = Q(3, 4*N)
    invoff = Q(1, 4*N)
    hdiag = Q(2)/mu - bdiag/mu**2
    hoff = -boff/mu**2
    moff = invoff - hoff
    r = lambda x: Q(1, x) - Q(2)/mu + Q(x)/mu**2
    f_sq = Q(q) + Q(5, 4*N*N)
    m_sq = q * r(1)**2 + r(N)**2 + r(2*N)**2
    Vdirect = 4*invoff**2
    Vcorr = 4*moff**2
    rho = 1 - 2*Q(N*N)/mu**2
    return locals()


def check():
    count = 0
    for N in range(2, 48):
        d = construction(N)
        q, n, mu, T, G = (d[k] for k in ('q', 'n', 'mu', 'T', 'G'))
        bd, bo, fi, fo, hd, ho, mo = (d[k] for k in
            ('bdiag', 'boff', 'invdiag', 'invoff', 'hdiag', 'hoff', 'moff'))
        # Direct exact inverse of high-frequency two-by-two block.
        assert bd*fi + bo*fo == 1
        assert bd*fo + bo*fi == 0
        count += 2
        # Spectrum and global Lanczos starting from the identity.
        assert bd + bo == N and bd-bo == 2*N
        assert n*mu == q + 2*bd
        assert T == q + 2*fi
        assert G == q*(2/mu - 1/mu**2) + 2*hd
        # Constant and linear terms have their exact matrix traces.
        assert G == n*2/mu - (q + 2*bd)/mu**2
        count += 5
        # Exact Hermite remainder formula, for all three eigenvalues.
        r = d['r']
        for val in (1, N, 2*N):
            assert r(val) == Q((val-mu)**2, 1)/(mu**2*val)
            assert r(val) >= 0
            count += 2
        assert d['m_sq'] == q*r(1)**2 + r(N)**2 + r(2*N)**2
        assert d['f_sq'] == q + 2*(fi**2+fo**2)
        count += 2
        # The sole offdiagonal causes the entire Rademacher fluctuation.
        rho = d['rho']
        assert mo == fo*rho
        assert d['Vcorr'] == d['Vdirect']*rho**2
        assert d['Vdirect'] == Q(1,4*N*N)
        count += 3
        # Exact sample error distributions, independently for any sample count.
        for s in (1, 2, 4, 7):
            mean0 = Q(0)
            vd = Q(0)
            vc = Q(0)
            for k in range(s+1):
                prob = Q(comb(s,k),2**s)
                sample_mean = Q(s-2*k,s)
                ed = 2*fo*sample_mean
                ec = 2*mo*sample_mean
                assert ec == rho*ed
                mean0 += prob*sample_mean
                vd += prob*ed**2
                vc += prob*ec**2
                count += 1
            assert mean0 == 0
            assert vd == d['Vdirect']/s
            assert vc == d['Vcorr']/s
            count += 3
        assert T-G == q*r(1)+r(N)+r(2*N)
        assert T >= G
        count += 2
        # Gaussian quadratic-form variance follows from eigenvalue squares.
        assert d['m_sq'] >= 0 and d['f_sq'] >= 0
        count += 1
    # Strict finite-instance variance inflation and simultaneous Gaussian relief.
    for N in range(2,48):
        d = construction(N)
        assert d['Vcorr'] > d['Vdirect']
        assert d['m_sq'] < d['f_sq']
        count += 2
    # Check exact closed forms over a wide spectral range, avoiding floats.
    for N in (2,3,4,10,100,1000):
        d=construction(N)
        mu=d['mu']
        ratio=(1-2*Q(N*N)/mu**2)**2
        assert ratio == d['Vcorr']/d['Vdirect']
        assert d['T']-d['G'] == Q(6*N**4-8*N**3+3*N**2+1,2*N*(N*N+3))
        assert d['T'] == N**3 + Q(3,2*N)
        count += 3
    # Two-point-spectral benchmark: the exact scalar is bounded by kappa - 1.
    for p in (1,2,3,7,40):
        for q in (1,2,9):
            for a,b in ((1,2),(1,4),(2,15)):
                mu=Q(p*a+q*b,p+q)
                coeff=1-Q(a*b)/mu**2
                kap=Q(b,a)
                assert abs(coeff) <= kap-1
                count += 1
    print('VERIFY_OK',count,'exact-rational assertions')

if __name__=='__main__':
    check()
