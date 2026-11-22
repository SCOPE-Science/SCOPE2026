"""Exact checks for binary three-window-defect universal cycles.

Public mathematical verification; Python 3 standard library only.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def deleted_sets(n):
    # n >= 3, alternating word 010.. and 101.., and both primitive 3-cycles.
    def cyclic_pattern(seed):
        return int((seed * (n // len(seed) + 2))[:n], 2)
    two = {cyclic_pattern('01'), cyclic_pattern('10')}
    three0 = {cyclic_pattern('001'), cyclic_pattern('010'), cyclic_pattern('100')}
    three1 = {cyclic_pattern('011'), cyclic_pattern('110'), cyclic_pattern('101')}
    return [('loop0', two | {0}), ('loop1', two | {(1 << n) - 1}),
            ('cycle001', three0), ('cycle011', three1)]


def bareiss(a):
    a = [row[:] for row in a]
    N = len(a)
    if N == 0:
        return 1
    d, sign = 1, 1
    for k in range(N - 1):
        if a[k][k] == 0:
            j = next((i for i in range(k + 1, N) if a[i][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, N):
            for j in range(k + 1, N):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % d == 0
                a[i][j] = numerator // d
            a[i][k] = 0
        d = pivot
    return sign * a[N - 1][N - 1]


def arborescences(n, missing):
    m, mask = n - 1, (1 << (n - 1)) - 1
    vcount = 1 << m
    L = [[0] * vcount for _ in range(vcount)]
    for e in range(1 << n):
        if e in missing:
            continue
        i, j = e >> 1, e & mask
        L[i][i] += 1
        L[i][j] -= 1
    return bareiss([row[:-1] for row in L[:-1]])


def formula_ratios(n):
    m = n - 1
    z = Fraction(1, 2 ** m)
    two = (1 + 2 * (Fraction(-1, 2) ** m)) / 3
    s = (0, 1, -1)[m % 3]
    three = (1 + 2 * s * z - 8 * z * z) / 7
    return two, three


def count_tours(n, missing):
    # Every Euler cycle has exactly one occurrence of the least retained edge.
    present = [e for e in range(1 << n) if e not in missing]
    first = present[0]
    initial_vertex, current_vertex = first >> 1, first & ((1 << (n - 1)) - 1)
    out = [[] for _ in range(1 << (n - 1))]
    for e in present:
        out[e >> 1].append(e)
    remaining = sum(1 << e for e in present if e != first)

    @lru_cache(None)
    def dfs(v, rem):
        if rem == 0:
            return int(v == initial_vertex)
        ans = 0
        for e in out[v]:
            if (rem >> e) & 1:
                ans += dfs(e & ((1 << (n - 1)) - 1), rem ^ (1 << e))
        return ans
    return dfs(current_vertex, remaining)


def main():
    counts = []
    for n in range(3, 9):
        B = 2 ** (2 ** (n - 1) - n)
        R2, R3 = formula_ratios(n)
        expected = [B * R2, B * R2, B * R3, B * R3]
        assert all(x.denominator == 1 for x in expected)
        got = []
        for i, (name, miss) in enumerate(deleted_sets(n)):
            assert len(miss) == 3
            t = arborescences(n, miss)
            assert t == expected[i], (n, name, t, expected[i])
            got.append(t)
            if n <= 5:
                independent = count_tours(n, miss)
                assert independent == t, (n, name, independent, t)
        counts.append((n, sum(got)))
        if n <= 5:
            # Exhaustive independent balance classification of all triples.
            balanced = set()
            for triple in combinations(range(1 << n), 3):
                deg = [0] * (1 << (n - 1))
                for e in triple:
                    deg[e >> 1] += 1
                    deg[e & ((1 << (n - 1)) - 1)] -= 1
                if not any(deg):
                    balanced.add(frozenset(triple))
            assert balanced == {frozenset(s) for _, s in deleted_sets(n)}
    assert counts[:4] == [(3, 2), (4, 12), (5, 2176), (6, 59768832)], counts
    # Formula 3-cycle as a finite 3x3 determinant with overlaps of periodic words.
    for m in range(2, 16):
        p = '001'
        words = [(p * (m // 3 + 3))[i:i + m] for i in range(3)]
        Z = [[Fraction(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                Z[i][j] = sum((Fraction(1, 2 ** k) for k in range(m)
                                if words[i][k:] == words[j][:m-k]), Fraction(0))
        B = [[Fraction(int(i == j)) - (Z[i][j] - Z[(i + 1) % 3][j]) / 2
              for j in range(3)] for i in range(3)]
        det = (B[0][0]*(B[1][1]*B[2][2]-B[1][2]*B[2][1])
               - B[0][1]*(B[1][0]*B[2][2]-B[1][2]*B[2][0])
               + B[0][2]*(B[1][0]*B[2][1]-B[1][1]*B[2][0]))
        assert det == formula_ratios(m + 1)[1], (m, det)
    print('VERIFY_OK', 'exact_tree_orders=3..8', 'independent_Euler_tours=3..5',
          'complete_balanced_triples=3..5', 'periodic_overlap_m=2..15',
          'totals=' + repr(counts))


if __name__ == '__main__':
    main()
