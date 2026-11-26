"""Independent exhaustive checks of odd induced subsets of rook graphs.

Run with Python 3.9+ using the standard library: python rook_odd_verifier.py
Only small finite orders are tested; the unrestricted formula needs its proof.
"""
from itertools import product
from math import comb


def even_fibre_count(rows, columns):
    """Number of functions [rows] -> [columns] with even fibres."""
    dp = [0] * (rows + 1)
    dp[0] = 1
    for _ in range(columns):
        out = [0] * (rows + 1)
        for u in range(rows + 1):
            for j in range(0, rows - u + 1, 2):
                out[u + j] += dp[u] * comb(rows - u, j)
        dp = out
    return dp[rows]


def theorem(m, n):
    if m > n:
        m, n = n, m
    if (m + n) & 1:
        return m * n, 1
    if m == n == 1:
        return 0, 1
    base = n if (m & 1) else even_fibre_count(m, n)
    return m * n - m, base * (2 if m == n else 1)


def predicted_deleted(m, n):
    """Construct precisely the predicted complements, independent of edge tests."""
    if (m + n) & 1:
        return {0}
    if m > n:
        masks = predicted_deleted(n, m)
        ans = set()
        for oldmask in masks:
            mask = 0
            for i in range(n):
                for j in range(m):
                    if oldmask & (1 << (i * m + j)):
                        mask |= 1 << (j * n + i)
            ans.add(mask)
        return ans
    if m == n == 1:
        return {1}
    ans = set()
    for assignment in product(range(n), repeat=m):
        freq = [assignment.count(j) for j in range(n)]
        if m % 2 == 0:
            if any(k % 2 for k in freq):
                continue
        else:
            if max(freq) != m:
                continue
        mask = sum(1 << (i * n + assignment[i]) for i in range(m))
        ans.add(mask)
    if m == n:
        for oldmask in list(ans):
            mask = 0
            for i in range(m):
                for j in range(n):
                    if oldmask & (1 << (i * n + j)):
                        mask |= 1 << (j * n + i)
            ans.add(mask)
    return ans


def independently_exhaust(m, n):
    N = m * n
    neighbours = [0] * N
    for u in range(N):
        ui, uj = divmod(u, n)
        for v in range(N):
            vi, vj = divmod(v, n)
            if u != v and (ui == vi or uj == vj):
                neighbours[u] |= 1 << v
    maximum, complements = -1, set()
    for chosen in range(1 << N):
        if any((neighbours[u] & chosen).bit_count() % 2 != 1
               for u in range(N) if chosen & (1 << u)):
            continue
        size = chosen.bit_count()
        if size > maximum:
            maximum, complements = size, set()
        if size == maximum:
            complements.add(((1 << N) - 1) ^ chosen)
    return maximum, complements


def main():
    cases, exact_sets = 0, 0
    for m in range(1, 5):
        for n in range(m, 7):
            if m * n > 20:
                continue
            maximum, actual = independently_exhaust(m, n)
            proposed = predicted_deleted(m, n)
            expected_max, expected_count = theorem(m, n)
            assert (maximum, len(actual)) == (expected_max, expected_count), (m, n, maximum, len(actual))
            assert actual == proposed, (m, n, len(actual ^ proposed))
            cases += 1
            exact_sets += len(actual)
    print('PASS:', cases, 'exhaustive graph sizes;', exact_sets,
          'maximizing vertex sets matched exactly, including their identity')
    for m, n in [(4, 6), (5, 5), (6, 6), (6, 12), (8, 8)]:
        print('m,n,maximum,count:', m, n, *theorem(m, n))


if __name__ == '__main__':
    main()
