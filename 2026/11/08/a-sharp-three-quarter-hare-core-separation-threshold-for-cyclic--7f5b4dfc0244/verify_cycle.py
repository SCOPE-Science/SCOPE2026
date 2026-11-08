"""Reproducible finite checks for the cyclic two-approval Hare-core boundary.
Only integer arithmetic; the infinite theorem is proved separately.
Run: python3 verify_cycle.py
"""
from itertools import combinations
from random import Random


def mask(n, positions):
    return sum(1 << i for i in positions)


def rotate_one(x, n):
    allbits = (1 << n) - 1
    return ((x << 1) | (x >> (n - 1))) & allbits


def improved(W, T, n):
    allbits = (1 << n) - 1
    wleft, tleft = rotate_one(W, n), rotate_one(T, n)
    unrepresented = (~(W | wleft)) & allbits
    singly = W ^ wleft
    touched = T | tleft
    doubled = T & tleft
    return ((unrepresented & touched) | (singly & doubled)).bit_count()


def ejr(W, n, k):
    # Each pair of distinct voter approvals intersects in at most one candidate.
    if 2 * k < n:
        return True
    return all(any(W & (1 << ((c + delta) % n))
                   for delta in (-1, 0, 1)) for c in range(n))


def core(W, n, k):
    for T in range(1, 1 << n):
        t = T.bit_count()
        if t >= k:
            continue
        if k * improved(W, T, n) >= n * t:
            return False
    return True


def construct(n, k):
    z = n - k
    assert n >= 16 and (3*n + 3)//4 <= k <= n - 4
    zeros = {0, 1, 3, 4}
    zeros.update(range(7, 7 + 3 * (z - 4), 3))
    assert len(zeros) == z
    return mask(n, set(range(n)) - zeros)


def check():
    total_checked = 0
    for n in range(4, 11):
        for k in range(1, n + 1):
            for ids in combinations(range(n), k):
                W = mask(n, ids)
                if ejr(W, n, k):
                    is_core = core(W, n, k)
                    expected = not (4*k >= 3*n and n-k >= 4)
                    if expected:
                        assert is_core, (n, k, ids)
                total_checked += 1
    print('exhaustive committees n=4..10:', total_checked)
    # Exact boundary witness at n=16, k=12.
    n, k = 16, 12
    W = construct(n, k)
    T = mask(n, [1, 2, 3])
    assert ejr(W, n, k)
    assert improved(W, T, n) == 4
    assert k * 4 == n * 3
    assert not core(W, n, k)
    print('sharp witness n=16,k=12: 4 voters improve via 3 candidates')
    constructions = 0
    for n in range(16, 100):
        for k in range((3*n + 3)//4, n - 3):
            W = construct(n, k)
            T = mask(n, [1, 2, 3])
            assert ejr(W, n, k)
            assert improved(W, T, n) == 4
            assert 4 * k >= 3 * n
            constructions += 1
    print('all constructive parameter pairs n=16..99:', constructions)
    rng = Random(20261102)
    bound_checks = 0
    for n in range(4, 75):
        for _ in range(80):
            # Only sample absent-candidate patterns with no cyclic triple zeros.
            W = rng.getrandbits(n)
            if any(not any(W & (1 << ((c + delta) % n))
                           for delta in (-1, 0, 1)) for c in range(n)):
                continue
            T = rng.getrandbits(n) & ((1 << n) - 1)
            t = T.bit_count()
            if 0 < t < n:
                assert 3 * improved(W, T, n) <= 4 * t, (n, W, T)
                bound_checks += 1
    print('random 4/3-bound checks:', bound_checks)
    print('PASS')


if __name__ == '__main__':
    check()
