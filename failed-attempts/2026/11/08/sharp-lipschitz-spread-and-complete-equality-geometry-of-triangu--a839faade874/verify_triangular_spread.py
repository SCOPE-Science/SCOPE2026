"""Exact checks for triangular-graph 1-Lipschitz variance.

No external dependencies. Enumeration is finite corroboration; the result
for every n>=4 follows from the algebraic proof in RESULT.md.
"""
from itertools import combinations
from math import comb


def expected_numerator(n):
    assert n >= 4
    N = comb(n, 2)
    k = n // 2
    if n % 2:
        return k * k * (N - 1)
    return N * k * (k - 1)


def enumerate_integer_profiles(n):
    verts = list(combinations(range(n), 2))
    N = len(verts)
    adjacency = []
    for i, e in enumerate(verts):
        adjacency.append([j for j in range(i)
                          if bool(set(e) & set(verts[j]))])
    assigned = [0] * N
    counts = [0, 0, 0]
    best = -1
    multiplicity = 0
    visited = 0

    def extend(i):
        nonlocal best, multiplicity, visited
        if i == N:
            if counts[0] == 0 or counts[2] == 0:
                return
            visited += 1
            q = N * (counts[0] + counts[2]) - (counts[0] - counts[2]) ** 2
            if q > best:
                best, multiplicity = q, 1
            elif q == best:
                multiplicity += 1
            return
        for v in range(3):
            if any(abs(v - assigned[j]) > 1 for j in adjacency[i]):
                continue
            assigned[i] = v
            counts[v] += 1
            extend(i + 1)
            counts[v] -= 1

    extend(0)
    return best, multiplicity, visited


def expected_maximizers(n):
    return (1 if n % 2 == 0 else 2) * comb(n, n // 2)


def capacity_check(up_to=300):
    comparisons = 0
    for n in range(4, up_to + 1):
        N = comb(n, 2)
        target = expected_numerator(n)
        for t in range(2, n // 2 + 1):
            A = comb(n - t, 2)
            B = comb(t, 2)
            D = A - B
            if 2 * D <= N:
                envelope = N * (A + B) - D * D
                assert envelope <= target
                if envelope == target:
                    assert t == n // 2
            else:
                # Strict comparison using four times the continuous envelope.
                assert N * N + 8 * N * B < 4 * target
            comparisons += 1
    return comparisons


def main():
    for n in (4, 5, 6):
        best, mult, visited = enumerate_integer_profiles(n)
        assert best == expected_numerator(n)
        assert mult == expected_maximizers(n)
        print('EXACT_ALL_INTEGER_EXTREMIZERS_OK', n, visited, mult)
    comparisons = capacity_check(300)
    print('EXACT_CAPACITY_ENVELOPE_INEQUALITIES_OK', comparisons)
    for n in range(4, 3001):
        N = comb(n, 2)
        q = expected_numerator(n)
        assert 4 * q > N * N
        if n % 2 == 0:
            assert 2 * (n - 1) * q == (n - 2) * N * N
        else:
            assert 2 * n * n * q == (n - 2) * (n + 1) * N * N
    print('EXACT_CLOSED_FORMS_AND_BINARY_SEPARATION_OK', 2997)
    print('ALL_TRIANGULAR_GRAPH_SPREAD_CHECKS_OK')


if __name__ == '__main__':
    main()
