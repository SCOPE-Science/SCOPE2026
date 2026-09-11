"""Lane-1029 verifier (stdlib only): constant-diagonal self-orthogonal impossibility.

Proves: for every n >= 2, no n x n Latin square can be simultaneously
self-orthogonal (orthogonal to its own transpose) and have constant diagonal.
A fortiori no 3-MOLS(10) contains such a member.
Also exhaustively checks n=2,3,4 and exhibits a SOLS(5) with transversal diagonal.
"""
import itertools
import sys

def is_latin(L):
    n = len(L)
    syms = set(range(n))
    for i in range(n):
        if set(L[i]) != syms:
            return False
    for j in range(n):
        if {L[i][j] for i in range(n)} != syms:
            return False
    return True

def is_self_orthogonal(L):
    n = len(L)
    seen = set()
    for i in range(n):
        for j in range(n):
            p = (L[i][j], L[j][i])
            if p in seen:
                return False
            seen.add(p)
    return len(seen) == n * n

def has_constant_diagonal(L):
    n = len(L)
    return all(L[i][i] == L[0][0] for i in range(n))

def diagonal_pair_multiplicity(L):
    n = len(L)
    c = L[0][0]
    return sum(1 for i in range(n) if (L[i][i], L[i][i]) == (c, c))

def check_general_lemma(n, c=0):
    # Constant-diagonal n x n array: pair (c,c) occurs at least n times
    # in the transpose superposition, so orthogonality needs n <= 1.
    L = [[(i + j) % n for j in range(n)] for i in range(n)]
    for i in range(n):
        L[i][i] = c
    m = diagonal_pair_multiplicity(L)
    assert m == n, (n, m)
    return (n >= 2) and (m > 1)

def enum_latin(n):
    # Backtracking row by row over all Latin squares with symbols 0..n-1.
    # Feasible for n <= 4 (576 squares). For n=3: 12 squares.
    grid = [[-1] * n for _ in range(n)]
    row_used = [[False] * n for _ in range(n)]
    col_used = [[False] * n for _ in range(n)]
    # Fix nothing (full enumeration); n small so fine.
    cells = [(i, j) for i in range(n) for j in range(n)]
    def rec(k):
        if k == len(cells):
            yield [row[:] for row in grid]
            return
        i, j = cells[k]
        for s in range(n):
            if not row_used[i][s] and not col_used[j][s]:
                grid[i][j] = s
                row_used[i][s] = col_used[j][s] = True
                yield from rec(k + 1)
                row_used[i][s] = col_used[j][s] = False
                grid[i][j] = -1
    yield from rec(0)

def main():
    out = []
    # 1. General counting lemma for n = 2..10
    for n in [2, 3, 4, 5, 10]:
        ok = check_general_lemma(n)
        assert ok, n
        out.append(f"lemma العامة n={n}: constant diagonal forces pair repeat x{n} -> not orthogonal: OK")

    # 2. Exhaustive n=2: all 2x2 Latin squares (2 of them)
    n2 = list(enum_latin(2))
    assert len(n2) == 2, len(n2)
    for L in n2:
        assert not (is_self_orthogonal(L) and has_constant_diagonal(L))
    out.append(f"exhaustive n=2: {len(n2)} Latin squares, none both SOLS+const-diag: OK")

    # 3. Exhaustive n=3: 12 Latin squares
    n3 = list(enum_latin(3))
    assert len(n3) == 12, len(n3)
    sols3 = [L for L in n3 if is_self_orthogonal(L)]
    for L in n3:
        assert not (is_self_orthogonal(L) and has_constant_diagonal(L))
    for L in sols3:
        assert len({L[i][i] for i in range(3)}) == 3  # SOLS diagonal is transversal
    out.append(f"exhaustive n=3: 12 squares, {len(sols3)} SOLS, none const-diag, all SOLS diagonals transversal: OK")

    # 4. Exhaustive n=4: 576 Latin squares
    n4 = list(enum_latin(4))
    assert len(n4) == 576, len(n4)
    sols4 = [L for L in n4 if is_self_orthogonal(L)]
    for L in n4:
        assert not (is_self_orthogonal(L) and has_constant_diagonal(L))
    for L in sols4:
        assert len({L[i][i] for i in range(4)}) == 4
    out.append(f"exhaustive n=4: 576 squares, {len(sols4)} SOLS, none const-diag: OK")

    # 5. Explicit SOLS(5) with transversal diagonal (class nonempty in general)
    # L[i][j] = i + 2j mod 5 (2 is a unit, 1-2^2 = -3 unit mod 5 -> self-orthogonal).
    S5 = [[(i + 2 * j) % 5 for j in range(5)] for i in range(5)]
    assert is_latin(S5)
    assert is_self_orthogonal(S5), "SOLS(5) check"
    assert len({S5[i][i] for i in range(5)}) == 5, "SOLS(5) diagonal transversal"
    assert not has_constant_diagonal(S5)
    out.append("witness SOLS(5) Latin + self-orthogonal + transversal (non-constant) diagonal: OK")

    # 6. Order-10 counting instance (the target order): 10 repeats of (c,c)
    n = 10
    assert check_general_lemma(n)
    out.append("target order n=10: any constant-diagonal square repeats a transpose-pair 10x: OK")

    # 7. Isotopism readings sanity: diagonal-distinctness (being a transversal)
    # is invariant under simultaneous row/column permutations and symbol
    # permutations, which are exactly the isotopisms preserving self-orthogonality.
    # Demo on the SOLS(5): permute rows/cols simultaneously and rename symbols;
    # self-orthogonality and diagonal-distinctness are both preserved, so no
    # self-orthogonal square can be isotoped (by SO-preserving maps) to a
    # constant-diagonal square.
    import random
    rng = random.Random(1029)
    perm = list(range(5))
    rng.shuffle(perm)
    sp = list(range(5))
    rng.shuffle(sp)
    M = [[sp[S5[perm[i]][perm[j]]] for j in range(5)] for i in range(5)]
    assert is_latin(M)
    assert is_self_orthogonal(M), "SO preserved under simultaneous perm + symbol perm"
    assert len({M[i][i] for i in range(5)}) == 5, "transversal diagonal preserved"
    out.append("normalization sanity: SO + transversal-diagonal invariant under SO-preserving isotopism: OK")

    print("\n".join(out))
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
