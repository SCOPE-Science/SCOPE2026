"""Exact verification for symmetry of three-consecutive hexagonal-number semigroups.

Python 3 standard library. No external data or services required.
"""
from math import gcd
from heapq import heappush, heappop

EXPECTED = {2, 3, 6, 7, 8, 18}

def hexagonal(n):
    return n * (2 * n - 1)

def gluing_witnesses(n):
    numbers = [hexagonal(j) for j in (n, n + 1, n + 2)]
    ans = []
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        d = gcd(numbers[i], numbers[j])
        if d <= 1 or gcd(d, numbers[k]) != 1:
            continue
        a, b, c = numbers[i] // d, numbers[j] // d, numbers[k]
        # This loop enumerates *all* nonnegative coefficient pairs.
        for u in range(c // a + 1):
            v, rem = divmod(c - u * a, b)
            if rem == 0 and v >= 0:
                ans.append((i, j, k, d, u, v))
    return ans

def apery_frobenius_genus(n):
    """Independent min-plus Dijkstra on residues modulo the least generator."""
    a, b, c = (hexagonal(j) for j in (n, n + 1, n + 2))
    INF = 10 ** 30
    dist = [INF] * a
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        val, r = heappop(heap)
        if val != dist[r]:
            continue
        for step in (b, c):
            rr = (r + step) % a
            vv = val + step
            if vv < dist[rr]:
                dist[rr] = vv
                heappush(heap, (vv, rr))
    assert max(dist) < INF
    F = max(dist) - a
    numerator = 2 * sum(dist) - a * (a - 1)
    assert numerator % (2 * a) == 0
    genus = numerator // (2 * a)
    return F, genus

def main():
    assert 30 * (hexagonal(127) - hexagonal(125)) < hexagonal(125)
    assert hexagonal(125) == 31125
    assert hexagonal(127) - hexagonal(125) == 1006
    observed = set()
    samples = {}
    for n in range(2, 125):
        a, b, c = [hexagonal(j) for j in (n, n+1, n+2)]
        assert gcd(a, gcd(b, c)) == 1
        assert gcd(a, b) == gcd(n + 1, 3)
        assert gcd(b, c) == gcd(n + 2, 3)
        assert gcd(a, c) == gcd(n, 6) * gcd(n + 2, 5)
        if n >= 4:
            assert c < 3 * a and c < a + b and c < 2 * b
            assert c != 2 * a
        w = gluing_witnesses(n)
        if w:
            observed.add(n)
            samples[n] = w[0]
    assert observed == EXPECTED, (sorted(observed), sorted(EXPECTED))
    independent = set()
    for n in range(2, 61):
        F, genus = apery_frobenius_genus(n)
        if 2 * genus == F + 1:
            independent.add(n)
        assert (n in EXPECTED) == (2 * genus == F + 1), (n, F, genus)
    assert independent == EXPECTED
    print('Finite gluing classification: n=2..124, exact exhaustive: PASS')
    print('Independent Apéry genus/Frobenius classification: n=2..60: PASS')
    print('Exactly symmetric indices:', sorted(observed))
    print('Witnesses (i,j,k,d,u,v):', samples)
    print('Large-n proof constants: d <= 30; cutoff n >= 125: PASS')

if __name__ == '__main__':
    main()
