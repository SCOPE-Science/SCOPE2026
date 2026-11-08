"""Independent finite checks for the permutation-power first-disagreement theorem.

Run: python verify_distinguishing_spectrum.py
No third-party dependencies or source downloads are required.
"""
from itertools import combinations, permutations, product
from math import comb


def is_subsequence(pattern, host):
    """Literal left-to-right embedding test, separate from the proof formula."""
    j = 0
    for x in host:
        if j < len(pattern) and pattern[j] == x:
            j += 1
    return j == len(pattern)


def inversion_edges(p, q):
    rankp = {a: i for i, a in enumerate(p)}
    rankq = {a: i for i, a in enumerate(q)}
    return {frozenset((a, b)) for a, b in combinations(p, 2)
            if (rankp[a] - rankp[b]) * (rankq[a] - rankq[b]) < 0}


def independent_counts(p, q):
    edges = inversion_edges(p, q)
    counts = [1]
    for j in range(1, len(p) + 1):
        counts.append(sum(all(frozenset((a, b)) not in edges
                              for a, b in combinations(S, 2))
                          for S in combinations(p, j)))
    return counts


def predicted(p, q, r):
    n = len(p)
    independent = independent_counts(p, q)
    common_absent = sum(independent[j] * comb(r, j - 1)
                        for j in range(1, min(n, r + 1) + 1))
    return 2 * (comb(r + n, n - 1) - common_absent)


def exhaustive():
    cases = words = 0
    for n in range(2, 6):
        p = tuple(range(n))
        for q in permutations(p):
            for r in range(1, 4 if n == 5 else 5):
                x, y = p * r, q * r
                length = r + 1
                observed = sum(is_subsequence(u, x) != is_subsequence(u, y)
                               for u in product(p, repeat=length))
                assert observed == predicted(p, q, r), (n, q, r, observed)
                assert (observed == 0) == (p == q)
                cases += 1
                words += n ** length
    return cases, words


def extremal_and_reconstruction():
    tests = 0
    for n in range(2, 8):
        p = tuple(range(n))
        for q in permutations(p):
            ic = independent_counts(p, q)
            values = [predicted(p, q, r) for r in range(n)]
            # Newton differences recover the nonempty independence numbers.
            J = [comb(r + n, n - 1) - values[r] // 2 for r in range(n)]
            got = []
            for _ in range(n):
                got.append(J[0])
                J = [b - a for a, b in zip(J, J[1:])]
            assert got == ic[1:], (n, q, got, ic)
            edges = inversion_edges(p, q)
            assert values[1] == 2 * len(edges)
            for r in (1, 2, 5):
                d = predicted(p, q, r)
                if not edges:
                    assert d == 0
                else:
                    lo = 2 * comb(r + n - 2, n - 1)
                    hi = 2 * (comb(r + n, n - 1) - n)
                    assert lo <= d <= hi
                    assert (d == lo) == (len(edges) == 1)
                    assert (d == hi) == (len(edges) == comb(n, 2))
            tests += 1
    return tests


if __name__ == "__main__":
    cases, words = exhaustive()
    tests = extremal_and_reconstruction()
    print(f"PASS: {cases} exhaustive parameter cases, {words} literal candidate words")
    print(f"PASS: {tests} independence-reconstruction and extremality configurations")
    print("FINITE CHECK ONLY: the universal theorem rests on its separate proof.")
