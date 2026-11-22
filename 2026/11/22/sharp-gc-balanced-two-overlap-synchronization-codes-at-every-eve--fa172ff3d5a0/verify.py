"""Exact finite boundary certificate for GC-balanced two-overlap-free codes.

Run: python3 verify.py. Standard library only. Symbols 0,1 are AT; 2,3 are CG.
"""
from itertools import product
from math import comb

SIGMA = tuple(range(4))


def gc(word):
    return sum(x >= 2 for x in word)


def templates():
    # Each status entry: 0 unused first/last, 1 permitted first, 2 permitted last.
    for status in product((0, 1, 2), repeat=4):
        I = tuple(a for a in SIGMA if status[a] == 1)
        J = tuple(a for a in SIGMA if status[a] == 2)
        if not I or not J:
            continue
        common = tuple(product(I, J))
        for assignment in product((0, 1), repeat=len(common)):
            # 0 assigns pair to prefixes; 1 to suffixes.
            owner = dict(zip(common, assignment))
            P = frozenset(
                (a, b) for a in I for b in SIGMA
                if owner.get((a, b), 0) == 0
            )
            S = frozenset(
                (c, d) for c in SIGMA for d in J
                if owner.get((c, d), 1) == 1
            )
            assert P.isdisjoint(S)
            yield status, assignment, P, S


def boundary_coefficients(P, S):
    f = [0] * 5
    for a, b in P:
        for c, d in S:
            f[gc((a, b, c, d))] += 1
    return f


def exact_size(f, n):
    assert n >= 4 and n % 2 == 0
    L = n-4
    return 2**L * sum(
        f[j] * comb(L, n//2-j)
        for j in range(5) if 0 <= n//2-j <= L
    )


def formula(n):
    L = n - 4
    return 2**L * (20*comb(L, L//2)
                   + 16*(comb(L, L//2-1) if L >= 2 else 0))


def direct_count(P, S, n):
    return sum(1 for w in product(SIGMA, repeat=n)
               if gc(w) == n//2
               and tuple(w[:2]) in P
               and tuple(w[-2:]) in S)


def main():
    rows = list(templates())
    assert len(rows) == 280, len(rows)
    all_f = [boundary_coefficients(P, S) for _, _, P, S in rows]
    maxima = (
        max(f[2] for f in all_f),
        max(f[1]+f[2]+f[3] for f in all_f),
        max(sum(f) for f in all_f)
    )
    assert maxima == (20, 36, 36), maxima
    maximizers = [i for i, f in enumerate(all_f)
                  if f[2] == 20 and f[1]+f[2]+f[3] == 36]
    assert len(maximizers) == 12
    assert all(all_f[i] == [0, 8, 20, 8, 0] for i in maximizers)
    assert all(rows[i][0] in ((1,1,2,2), (2,2,1,1)) for i in maximizers)
    # At n=4 the central degree coefficient is decisive. For n>4,
    # r1>0 and the three coefficient bounds imply global optimality.
    for n in range(4, 28, 2):
        observed = max(exact_size(f, n) for f in all_f)
        assert observed == formula(n), (n, observed, formula(n))
        assert sum(exact_size(f, n) == observed for f in all_f) == 12
    # Independent word-level enumeration, not using coefficient convolution.
    for n in (4, 6):
        for (_, _, P, S), f in zip(rows, all_f):
            assert direct_count(P, S, n) == exact_size(f, n)
    # Explicit attaining boundary sets.
    P = frozenset([(0, b) for b in SIGMA] + [(1, 0), (1, 1)])
    S = frozenset([(c, d) for c in (1, 2, 3) for d in (2, 3)])
    assert boundary_coefficients(P, S) == [0, 8, 20, 8, 0]
    # Distinct actual optimum codes at n=4 and n=6.
    for n in (4, 6):
        codes = []
        for i in maximizers:
            _, _, p, s = rows[i]
            code = frozenset(w for w in product(SIGMA, repeat=n)
                             if gc(w) == n//2
                             and w[:2] in p and w[-2:] in s)
            codes.append(code)
        assert len(set(codes)) == 12
    print('PASS: 280 boundary templates; upper coefficients (20,36,36).')
    print('PASS: 12 distinct maximizing templates; all even lengths n>=4.')
    print('PASS: independent exhaustive word checks for n=4 and n=6.')
    print('Sizes:', {n: formula(n) for n in range(4, 16, 2)})


if __name__ == '__main__':
    main()
