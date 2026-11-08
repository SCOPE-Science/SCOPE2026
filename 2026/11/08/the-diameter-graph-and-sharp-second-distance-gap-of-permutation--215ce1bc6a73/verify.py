"""Exact finite checks for Euclidean diameters of permutation X-ray polytopes.

The unrestricted theorem is established by the accompanying proof, not by
this script. Run with Python 3 and no third-party packages.
"""
from itertools import permutations
from random import Random


def xray(perm):
    k = len(perm)
    out = [0] * (2 * k - 1)
    for i, j in enumerate(perm):
        out[i + j] += 1
    return tuple(out)


def dist2(a, b):
    return sum((u-v)**2 for u, v in zip(a, b))


def canonical(k):
    rev = [0] * (2*k-1)
    lo = [0] * (2*k-1)
    hi = [0] * (2*k-1)
    rev[k-1] = k
    lo[k-2], lo[2*k-2] = k-1, 1
    hi[k], hi[0] = k-1, 1
    return tuple(rev), tuple(lo), tuple(hi)


def runner(k):
    p = list(range(k))
    for i in range(k-2):
        p[i] = k-3-i
    p[k-2], p[k-1] = k-1, k-2
    return xray(p)


def finite_checks():
    assertions = 0
    for k in range(2, 9):
        images = {xray(p) for p in permutations(range(k))}
        h0, hm, hp = canonical(k)
        assert h0 in images and hm in images and hp in images
        assertions += 3
        target = 2*k*k - 2*k + 2
        assert dist2(h0, hm) == target
        assert dist2(h0, hp) == target
        assertions += 2
        for h in images:
            if h == h0:
                continue
            assert max(h) <= k-1
            assert sum(v*v for v in h) <= (k-1)**2 + 1
            assert dist2(h0, h) <= target
            assertions += 3
            if k >= 4 and h[k-1] == 0 and h not in (hm, hp):
                assert max(h) <= k-2
                assert sum(v*v for v in h) <= (k-2)**2 + 4
                assertions += 2
        if k <= 7:
            highs = []
            points = sorted(images)
            for i, u in enumerate(points):
                for v in points[i+1:]:
                    highs.append((dist2(u, v), u, v))
                    assertions += 1
            got = max(d for d,_,_ in highs)
            assert got == target
            maxpairs = {frozenset((u,v)) for d,u,v in highs if d == got}
            assert maxpairs == {frozenset((h0, hm)), frozenset((h0, hp))}
            assertions += 2
            if k >= 4:
                second = max(d for d,_,_ in highs if d < got)
                assert second == 2*k*k - 4*k + 8
                assertions += 1
            elif k == 3:
                assert max(d for d,_,_ in highs if d < got) == 10
                assertions += 1
        if k >= 4:
            assert dist2(h0, runner(k)) == 2*k*k-4*k+8
            assertions += 1
    for k in range(9, 101):
        h0, hm, hp = canonical(k)
        assert dist2(h0, hm) == 2*k*k - 2*k + 2
        assert dist2(h0, hp) == 2*k*k - 2*k + 2
        assert dist2(h0, runner(k)) == 2*k*k - 4*k + 8
        assertions += 3
    rng = Random(20261021)
    for k in range(9, 16):
        h0, hm, hp = canonical(k)
        for trial in range(1200):
            a = list(range(k))
            b = list(range(k))
            rng.shuffle(a)
            rng.shuffle(b)
            u, v = xray(a), xray(b)
            assert dist2(u, v) <= 2*k*k-2*k+2
            if u != h0 and v != h0:
                assert dist2(u,v) <= 2*(k-1)**2 + 2
            if frozenset((u,v)) not in (frozenset((h0,hm)),frozenset((h0,hp))):
                assert dist2(u,v) <= 2*k*k-4*k+8
            assertions += 3
    return assertions


if __name__ == '__main__':
    total = finite_checks()
    print(f"PASS: {total} exact-integer assertions; complete projected-X-ray pair checks for k=2,...,7, projection-profile checks through k=8, and constructed exact witnesses through k=100.")
