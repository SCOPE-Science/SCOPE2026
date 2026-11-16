"""Standalone exact-arithmetic consistency checks for two-radius Wiener interpolation.
The continuum proof is in RESULT.md; these tests are finite corroboration, not a proof.
"""
from fractions import Fraction as F
import math


def coeff(u, v, k):
    assert F(0) < u < v < F(1) and k >= 2
    d = u*v**k-v*u**k
    assert d > 0
    p = (v**k-u**k)/d
    q = (v-u)/d
    return p, q, p+q


def dual(u, v, k):
    d = u*v**k-v*u**k
    lam = -(v**k+v)/d
    mu = (u**k+u)/d
    return lam, mu


def check_pair(u, v, cutoff=64):
    scores = [coeff(u,v,k)[2] for k in range(2,cutoff+1)]
    best = min(scores)
    ks = [k for k in range(2,cutoff+1) if coeff(u,v,k)[2] == best]
    assert len(ks) in (1,2)
    if len(ks)==2:
        assert ks[1] == ks[0]+1
    for k in ks:
        p, q, score = coeff(u,v,k)
        assert 1-p*u+q*u**k == 0
        assert 1-p*v+q*v**k == 0
        lam, mu = dual(u,v,k)
        assert lam*u+mu*v == -1
        assert lam*u**k+mu*v**k == 1
        assert -(lam+mu) == score
        # A finite exact check; the infinite dual inequalities are proved in RESULT.md.
        for j in range(1,cutoff+1):
            hj = lam*u**j+mu*v**j
            assert -1 <= hj <= 1
        assert all(lam*u**j+mu*v**j > -1 for j in range(2,cutoff+1))
    return len(ks)


def run():
    pairs = 0
    tie_pairs = 0
    for a in range(1,10):
        for b in range(a+1,11):
            u, v = F(a,11), F(b,11)
            tie_pairs += check_pair(u,v)
            pairs += 1
    # An exact endpoint tie: u+v+uv=1.
    u,v=F(1,5), F(2,3)
    k2=coeff(u,v,2)
    k3=coeff(u,v,3)
    assert k2[2] == k3[2]
    assert check_pair(u,v) == 2
    assert u+v+u*v == 1
    # Signed endpoint algebra and the first transition.
    for a in range(1,10):
        for b in range(a+1,11):
            u,v=F(a,11),F(b,11)
            left=coeff(u,v,2)[2]-coeff(u,v,3)[2]
            right=(u+v+u*v-1)/(u*v*(u+v))
            assert left==right
    # A regime with high-degree optimal three-term polynomial.
    u,v=F(4,5),F(9,10)
    ks=[k for k in range(2,31) if coeff(u,v,k)[2] == min(coeff(u,v,j)[2] for j in range(2,31))]
    assert ks == [9]
    print('CHECK_OK exact_pairs=',pairs,' exact_tie=',len(ks),' high_degree_k=',ks[0])

if __name__ == '__main__':
    run()
