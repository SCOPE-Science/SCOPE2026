"""Exact rational consistency tests for the half-density Haar Gabor spectrum.

This finite checker tests coefficient identities and endpoint envelopes;
its calculations do not prove the operator-theoretic theorem.
"""
from fractions import Fraction as F


def haar(t):
    if -F(1, 2) <= t < 0:
        return -1
    if 0 <= t < F(1, 2):
        return 1
    return 0


def coeff(b, t, ell):
    a = F(1, 2) / b
    q = 1 / b
    lo = int((t-F(1,2))/a)-5
    hi = int((t+F(1,2))/a)+5
    return sum(haar(t-n*a)*haar(t-n*a-ell*q) for n in range(lo,hi+1))


def spectrum_bounds(b):
    if b < F(1,2):
        return F(0), 1/b
    if b == F(1,2) or b == 1:
        return F(2), F(2)
    if b < 1:
        return 1/b, 2/b
    if b <= F(3,2):
        return 1/b, 5/b
    if b <= 2:
        return F(0), 8/b
    raise ValueError('Outside specified range')


def attainable_M(b):
    if b == 1:
        return {0}
    if b == F(3,2):
        return {1}
    if b == 2:
        return {2}
    if 1 < b < F(3,2):
        return {0,1}
    if F(3,2) < b < 2:
        return {1,2}
    raise ValueError


cases = 0
bs = [F(2,5),F(1,2),F(3,5),F(3,4),F(9,10), F(1),
      F(11,10),F(6,5),F(7,5),F(3,2),F(8,5),F(7,4),F(19,10),F(2)]
for b in bs:
    a=1/(2*b)
    q=1/b
    gs = set()
    ms = set()
    for j in range(300):
        # Offset avoids the ordinary rational boundary grid in most samples;
        # exact half-open conventions handle boundary coincidences regardless.
        t = (F(j,300)+F(1,100003))*a
        gm = [coeff(b,t,k) for k in range(-3,4)]
        assert gm[3] >= 0
        for k in [-3,-2,2,3]:
            assert gm[k+3] == 0, (b,t,k,gm)
        assert gm[2] == gm[4], (b,t,gm)
        gs.add(gm[3])
        cases += 7
        if b <= 1:
            assert gm[2] == gm[4] == 0
            assert gm[3] in ({0,1} if b<F(1,2) else {1} if b==F(1,2) else {1,2} if b<1 else {2})
        else:
            m=-gm[4]
            assert gm[3] == 2+m
            ms.add(m)
            assert m in attainable_M(b)
            cases += 2
    if b>1:
        assert ms == attainable_M(b),(b,ms,attainable_M(b))
        candidates = [(2+m-2*m*c)/b for m in ms for c in (F(-1),F(1))]
        assert (min(candidates), max(candidates)) == spectrum_bounds(b)
        cases+=2
    else:
        should={0,1} if b<F(1,2) else {1} if b==F(1,2) else {1,2} if b<1 else {2}
        assert gs==should, (b,gs,should)
        assert (min(gs)/b,max(gs)/b)==spectrum_bounds(b)
        cases+=2
print('HAAR_GABOR_RATIONAL_CHECKS_PASS',cases)
