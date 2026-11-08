"""Finite reproducibility checks for layered twinned-chain incenter geometry.

Uses only Python's standard library.  These are finite checks, not a proof
for arbitrary layer sizes; the written analytic argument supplies that proof.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from math import prod

getcontext().prec = 62
ZERO = Decimal(0)
ONE = Decimal(1)
EPS = Decimal('1e-48')


def factor_vertices(m):
    if m == 1:
        return [(-1,), (1,)]
    vs = []
    for i in range(m):
        for sign in (-1, 1):
            a = [0] * m
            a[i] = sign
            vs.append(tuple(a))
    for i in range(m):
        for j in range(m):
            if i != j:
                a = [0] * m
                a[i], a[j] = 1, -1
                vs.append(tuple(a))
    assert len(vs) == m * (m + 1)
    return vs


def vertices(layer_sizes):
    for blocks in product(*(factor_vertices(m) for m in layer_sizes)):
        yield tuple(t for block in blocks for t in block)


def rational_rank(rows):
    arr = [[Fraction(x) for x in row] for row in rows]
    if not arr:
        return 0
    rank = 0
    n = len(arr[0])
    for col in range(n):
        pivot = next((j for j in range(rank, len(arr)) if arr[j][col]), None)
        if pivot is None:
            continue
        arr[rank], arr[pivot] = arr[pivot], arr[rank]
        k = arr[rank][col]
        arr[rank] = [z / k for z in arr[rank]]
        for j in range(len(arr)):
            if j != rank:
                k = arr[j][col]
                if k:
                    arr[j] = [a - k*b for a,b in zip(arr[j], arr[rank])]
        rank += 1
    return rank


def test_profile(ms):
    n = sum(ms)
    wide = [m for m in ms if m >= 2]
    s = sum(m == 1 for m in ms)
    w = len(wide)
    H = s + 2*w
    radius = ONE / Decimal(H).sqrt()
    tau = ONE - (ONE - ONE/Decimal(H)).sqrt() if w else ZERO
    vv = list(vertices(ms))
    assert len(vv) == prod(len(factor_vertices(m)) for m in ms)
    nsq = [sum(t*t for t in v) for v in vv]
    assert max(nsq) == H
    extreme = [v for v,ss in zip(vv, nsq) if ss == H]
    assert rational_rank(extreme) == n-w
    base_count = 2**s * prod(m*(m-1) for m in wide)
    assert len(extreme) == base_count
    centers = []
    for bits in product((-1,1), repeat=w):
        center = []
        i = 0
        for m in ms:
            if m == 1:
                center.append(ZERO)
            else:
                center.extend([Decimal(bits[i]) * tau] * m)
                i += 1
        centers.append(center)
    if not centers:
        centers = [[ZERO]*n]
    for c in centers:
        contacts = 0
        for v,ss in zip(vv, nsq):
            lhs = sum(Decimal(a)*b for a,b in zip(v,c)) + Decimal(ss).sqrt()*radius
            assert lhs <= ONE + EPS, (ms, lhs, v)
            if abs(lhs-ONE) <= EPS:
                contacts += 1
        expected = base_count + 2**s*sum(
            wide[i]*prod(wide[j]*(wide[j]-1) for j in range(w) if j!=i)
            for i in range(w)
        )
        assert contacts == expected, (ms, contacts, expected)
    return len(vv), len(centers)


def main():
    profiles = [(1,), (2,), (3,), (4,), (5,), (1,1), (1,2), (2,2),
                (2,3), (3,3), (1,1,2), (1,2,3), (2,2,2),
                (1,1,3,3), (2,3,2), (1,4,2), (3,2,3), (1,2,2,2),
                (1,1,4,2), (2,2,3), (3,3,2), (1,3,3), (1,1,1,2),
                (2,4), (4,4), (1,1,1,1), (2,2,2,2)]
    total = 0
    corners = 0
    for ms in profiles:
        nv, nc = test_profile(ms)
        total += nv
        corners += nc
    print('LAYERED_TWINNED_INCENTER_CHECKS_PASSED',
          'profiles=', len(profiles), 'polar_vertices=', total,
          'incenter_corners=', corners)


if __name__ == '__main__':
    main()
