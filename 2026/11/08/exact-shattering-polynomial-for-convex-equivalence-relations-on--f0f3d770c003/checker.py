"""Finite cross-checks for shattered equality-query supports of convex partitions.

Stdlib only. Run: python checker.py
The unrestricted proof is in RESULT.md; these are finite independent tests.
"""
from itertools import combinations
from collections import Counter
from math import comb


def intervals(N):
    return [(a, b) for a in range(N) for b in range(a, N)]


def private_criterion(N, subset, ranges):
    bitsets = [sum(1 << p for p in range(a, b + 1)) for a, b in ranges]
    for k in subset:
        others = 0
        for j in subset:
            if j != k:
                others |= bitsets[j]
        if bitsets[k] & ~others == 0:
            return False
    return True


def direct_shattered(N, subset, ranges):
    qs = [(1 << (b + 1)) - (1 << a) for (a,b) in ranges]
    outcomes = set()
    for cut in range(1 << N):
        word = tuple(int((cut & qs[j]) == 0) for j in subset)
        outcomes.add(word)
    return len(outcomes) == (1 << len(subset))


def formula(N, k):
    if k == 0:
        return 1
    if k > N:
        return 0
    return sum(comb(k - 1, j) * comb(N + k - j, 2 * k)
               for j in range(min(k-1, N-k) + 1))


def transfer(N):
    # Polynomial-weighted transfer across consecutive cut sites.
    A, B, D = [1], [0], [0]
    for _ in range(N):
        outA = [0] * (N + 1)
        outB = [0] * (N + 1)
        outD = [0] * (N + 1)
        for k in range(N + 1):
            a = A[k] if k < len(A) else 0
            b = B[k] if k < len(B) else 0
            d = D[k] if k < len(D) else 0
            outA[k] += a + b
            outB[k] += b + d
            outD[k] += d
            if k + 1 <= N:
                outB[k+1] += a + b
                outD[k+1] += b
        A, B, D = outA, outB, outD
    return [A[k] + B[k] for k in range(N+1)]


def main():
    for N in range(0, 6):
        ranges = intervals(N)
        counts = Counter()
        for size in range(len(ranges) + 1):
            for subset in combinations(range(len(ranges)), size):
                via_private = private_criterion(N, subset, ranges)
                via_all_labels = direct_shattered(N, subset, ranges)
                assert via_private == via_all_labels, (N, subset)
                if via_private:
                    counts[size] += 1
        exp = [formula(N, k) for k in range(N + 1)]
        assert [counts[k] for k in range(N + 1)] == exp, (N, counts, exp)
        assert transfer(N) == exp, N
        print('DIRECT', N, exp)
    for N in range(6, 31):
        exp = [formula(N, k) for k in range(N + 1)]
        assert transfer(N) == exp, N
        assert sum(exp) == (3 ** N + 1)//2
        assert exp[N] == 1
    print('CONVEX_EQUIVALENCE_INTERVAL_SHATTERING_PASS')

if __name__ == '__main__':
    main()
