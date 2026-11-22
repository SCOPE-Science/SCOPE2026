#!/usr/bin/env python3
"""Check the explicit cyclic-column quotient of the ordinary 3-by-n chessboard complex.

Standalone Python 3, standard library only. The mathematical all-n proof is in RESULT.md;
finite checks here are corroboration, not induction or a replacement for that proof.
"""
from itertools import combinations, permutations
from collections import defaultdict


def cells(n, k):
    result = set()
    orbit_multiplicity = defaultdict(int)
    for rows in combinations(range(3), k):
        for cols in permutations(range(n), k):
            key = (rows, tuple((x - cols[0]) % n for x in cols))
            result.add(key)
            orbit_multiplicity[key] += 1
    assert set(orbit_multiplicity.values()) == {n}
    return sorted(result)


def boundary_matrices(n):
    cell = {k: cells(n, k) for k in (1, 2, 3)}
    assert tuple(map(len, (cell[1], cell[2], cell[3]))) == \
           (3, 3 * (n - 1), (n - 1) * (n - 2))
    idx = {k: {v: i for i, v in enumerate(cell[k])} for k in (1, 2, 3)}
    D1 = [[0 for _ in cell[2]] for _ in cell[1]]
    D2 = [[0 for _ in cell[3]] for _ in cell[2]]
    for k, M in ((2, D1), (3, D2)):
        for j, (rows, offsets) in enumerate(cell[k]):
            for omit in range(k):
                rr = rows[:omit] + rows[omit + 1:]
                cc = offsets[:omit] + offsets[omit + 1:]
                normalized = tuple((c - cc[0]) % n for c in cc)
                i = idx[k - 1][(rr, normalized)]
                M[i][j] += (-1) ** omit
    for i in range(len(D1)):
        for j in range(len(D2[0])):
            assert sum(D1[i][a] * D2[a][j] for a in range(len(D2))) == 0
    return D1, D2


def mod_rank(A, p):
    B = [[v % p for v in r] for r in A]
    rows, cols = len(B), len(B[0])
    piv = 0
    for c in range(cols):
        cand = next((i for i in range(piv, rows) if B[i][c]), None)
        if cand is None: continue
        B[piv], B[cand] = B[cand], B[piv]
        q = pow(B[piv][c], -1, p)
        B[piv] = [(q * z) % p for z in B[piv]]
        for i in range(piv + 1, rows):
            if B[i][c]:
                f = B[i][c]
                B[i] = [(x - f * y) % p for x, y in zip(B[i], B[piv])]
        piv += 1
        if piv == rows: break
    return piv


def reduced_exponent(n, k):
    k %= n
    assert k != 0
    return -1 if k == n - 1 else k


def verify_symbolic_eliminations(n):
    """Independent check of the explicit sequence's indices and final degrees.
    Following the proof's elimination order, the surviving letters satisfy
       c_k=t^k (1<=k<=n-2), c_{n-1}=t^{-1}.
    We check every original triangle relator after the eliminated a,b letters,
    and account separately for each relator used to eliminate a letter.
    """
    assert n >= 5
    pairs = [(r, s) for r in range(1, n - 1)
                       for s in range(1, n - 1) if r != s]
    used_rec = {(1, s) for s in range(2, n - 1)}
    special = {(n - 2, 1), (2, 1)}
    assert not (used_rec & special)
    assert special <= set(pairs)
    E = lambda r, s: (reduced_exponent(n, s-r)
                      - reduced_exponent(n, -r)
                      - reduced_exponent(n, s))
    assert E(2, 1) == -n
    residual = [E(r, s) for r, s in pairs if (r, s) not in used_rec
                and (r, s) != (n-2, 1)]
    assert len(residual) == (n - 2) * (n - 4)
    assert all(x in (0, -n) for x in residual)
    assert -n in residual
    assert len(residual) - 1 == n*n - 6*n + 7
    assert 2 * (n - 2) + (n - 3) + 1 == 3*n-6
    return residual.count(-n), residual.count(0)


def main():
    for n in range(5, 101):
        nonzero, zeros = verify_symbolic_eliminations(n)
        if n in (5, 6, 7, 8, 9, 10):
            D1, D2 = boundary_matrices(n)
            assert mod_rank(D1, 2) == 2
            for p in (2, 3, 5, 7, 11):
                expect = 3*n - 6 if n % p == 0 else 3*n - 5
                assert mod_rank(D2, p) == expect, (n, p)
            print('n=%s; orbit cells=(3,%d,%d); degree-n cells=%d; zero cells=%d; modular checks PASS'
                  % (n, 3*(n-1), (n-1)*(n-2), nonzero, zeros))
    print('UNIFORM_SYMBOLIC_INDICES_CHECKED_n=5..100')
    print('THREE_ROW_CYCLIC_QUOTIENT_CHECKS_OK')


if __name__ == '__main__':
    main()
