"""Independent finite and arithmetic checks for consecutive pentagonal generators.

Standard-library only. Run with: python verify.py
The complete argument for indices above 70 is in RESULT.md; this checker
exhausts every index in the remaining finite interval and verifies examples.
"""

from heapq import heappop, heappush
from math import gcd


def p(n):
    assert n >= 1
    return n * (3 * n - 1) // 2


def pair_gluings(n):
    a, b, c = [p(n + k) for k in range(3)]
    answer = []
    for x, y, z in ((a, b, c), (a, c, b), (b, c, a)):
        d = gcd(x, y)
        if d < 2:
            continue
        u, v = x // d, y // d
        for beta in range(z // v + 1):
            residual = z - beta * v
            if residual >= 0 and residual % u == 0:
                alpha = residual // u
                if alpha + beta >= 2 and gcd(d, z) == 1:
                    answer.append((x, y, z, d, alpha, beta))
                    break
    return answer


def frobenius_and_twice_genus(n):
    a, b, c = [p(n + k) for k in range(3)]
    inf = 10**40
    dist = [inf] * a
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heappop(heap)
        if value != dist[residue]:
            continue
        for step in (b, c):
            new_residue = (residue + step) % a
            new_value = value + step
            if new_value < dist[new_residue]:
                dist[new_residue] = new_value
                heappush(heap, (new_value, new_residue))
    assert all(x < inf for x in dist)
    assert all(x % a == residue for residue, x in enumerate(dist))
    total = sum(dist)
    assert 2 * total % a == 0
    return max(dist) - a, 2 * total // a - (a - 1)


def main():
    assert 3 * 71**2 - 211 * 71 - 70 > 0
    assert 3 * 71**2 - 199 * 71 - 270 > 0
    assert 3 * 10**2 - 25 * 10 - 20 > 0
    assert 3 * 6**2 - 13 * 6 - 10 > 0
    # The quadratic left sides are strictly increasing beyond these thresholds.
    found = []
    for n in range(3, 71):
        if n == 5:  # third generator is twice the first
            continue
        a, b, c = [p(n + k) for k in range(3)]
        assert gcd(gcd(a, b), c) == 1
        representations = pair_gluings(n)
        if representations:
            found.append(n)
        assert (len(representations) > 0) == (n in (3, 40))
    assert found == [3, 40]
    assert (p(2), p(3), p(4)) == (5, 12, 22)
    assert p(4) == 2 * p(2) + p(3)
    assert (p(5), p(6), p(7)) == (35, 51, 70)
    assert p(7) == 2 * p(5)
    assert pair_gluings(3) == [(12, 22, 35, 2, 4, 1)]
    assert pair_gluings(40) == [(2380, 2625, 2501, 35, 7, 27)]
    symmetric = []
    f_values = {}
    for n in range(2, 71):
        f, two_g = frobenius_and_twice_genus(n)
        if two_g == f + 1:
            symmetric.append(n)
            f_values[n] = f
    assert symmetric == [2, 3, 5, 40]
    assert f_values == {2: 43, 3: 133, 5: 1699, 40: 258529}
    print('Finite-range gluing indices 3..70 except 5: [3, 40]')
    print('Independent Apery symmetric indices 2..70: [2, 3, 5, 40]')
    print('Exceptional Frobenius numbers:', f_values)
    print('All exact-arithmetic checks passed.')


if __name__ == '__main__':
    main()
