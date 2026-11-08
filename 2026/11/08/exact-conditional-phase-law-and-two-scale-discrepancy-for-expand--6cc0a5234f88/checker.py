#!/usr/bin/env python3
"""Exact arithmetic cross-check of interval-conditioned circle multiplication laws."""
from fractions import Fraction as Q
from math import gcd


def direct_distances(M, N, a, L):
    """Push forward a conditioned union of intervals, then integrate the density exactly."""
    assert 0 <= a < 1 and 0 < L < 1
    arcs = [(a, min(Q(1), a + L))]
    if a + L > 1:
        arcs.append((Q(0), a + L - 1))
    pieces = []
    for j in range(M):
        for aa, bb in arcs:
            lo, hi = (j + aa) / M, (j + bb) / M
            if lo == hi:
                continue
            low_k = (N * lo).numerator // (N * lo).denominator
            high_k = ((N * hi).numerator - 1) // (N * hi).denominator if (N * hi).denominator == 1 else (N * hi).numerator // (N * hi).denominator
            for k in range(low_k, high_k + 1):
                s, t = max(lo, Q(k, N)), min(hi, Q(k + 1, N))
                if t > s:
                    pieces.append((N * s - k, N * t - k))
    events = [(Q(0),0), (Q(1),0)]
    for lo, hi in pieces:
        events.append((lo,1))
        events.append((hi,-1))
    events.sort(key=lambda x: x[0])
    cur, total, value, cumulative, low, high = Q(0), 0, Q(0), Q(0), Q(0), Q(0)
    for endpoint, delta in events:
        if endpoint > cur:
            signed = (endpoint - cur) * (Q(total, N) / L - 1)
            value += abs(signed) / 2
            cumulative += signed
            low, high = min(low, cumulative), max(high, cumulative)
            cur = endpoint
        total += delta
    assert cur == 1 and total == 0 and cumulative == 0
    return value, high-low


def predicted_distances(M, N, L):
    v = N // gcd(M, N)
    t = v * L
    frac = t - (t.numerator // t.denominator)
    tv = frac * (1-frac) / t
    u = M // gcd(M,N)
    return tv, tv/u


def run():
    checks=0
    for b in (2,3,4):
        for n in range(1,5):
            for m in range(n+1,6):
                M,N=b**n-1,b**m-1
                for L in (Q(1,11),Q(1,7),Q(1,3),Q(2,5),Q(5,12)):
                    for a in (Q(0),Q(1,7),Q(4,5)):
                        direct=direct_distances(M,N,a,L)
                        pred=predicted_distances(M,N,L)
                        assert direct == pred, (b,n,m,a,L,direct,pred)
                        checks+=1
                v=N//gcd(M,N)
                for r in range(1,v):
                    if r>20: break
                    L=Q(r,v)
                    assert predicted_distances(M,N,L)==(0,0)
                    checks+=1
    # Complete example: M=3,N=7: interval length 2/7 makes later phase exactly Haar.
    assert direct_distances(3,7,Q(1,5),Q(2,7))==(0,0);checks+=1
    # Nonresonant case in which the early event almost pins down the later phase.
    assert direct_distances(3,7,Q(1,5),Q(1,70)) == (Q(9,10), Q(3,10)); checks+=1
    print('PASS',checks,'exact rational direct-pushforward, TV and arc-discrepancy checks')

if __name__=='__main__': run()
