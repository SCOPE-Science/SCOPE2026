"""Enumerate 4x4 quotient matrices R for symmetric 2-(36,15,6), classes 9^4.
Conditions: entries integers 0..9, row sums 15, col sums 15,
R R^T = 9 I + 54 J, R^T R = 9 I + 54 J. Pure python (no numpy)."""
import itertools

def row_types():
    out = set()
    for t in itertools.product(range(10), repeat=4):
        if sum(t) == 15 and sum(x * x for x in t) == 63:
            out.add(tuple(sorted(t)))
    return sorted(out)

def all_rows():
    out = []
    for t in itertools.product(range(10), repeat=4):
        if sum(t) == 15 and sum(x * x for x in t) == 63:
            out.append(t)
    return out

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def main():
    print("row types (sorted):", row_types())
    rows = all_rows()
    print("num ordered rows:", len(rows))
    sols = []
    for r1 in rows:
        for r2 in rows:
            if dot(r1, r2) != 54:
                continue
            for r3 in rows:
                if dot(r1, r3) != 54 or dot(r2, r3) != 54:
                    continue
                for r4 in rows:
                    if dot(r1, r4) != 54 or dot(r2, r4) != 54 or dot(r3, r4) != 54:
                        continue
                    M = [r1, r2, r3, r4]
                    ok = True
                    for j in range(4):
                        c = sum(M[i][j] for i in range(4))
                        q = sum(M[i][j] ** 2 for i in range(4))
                        if c != 15 or q != 63:
                            ok = False
                            break
                    if not ok:
                        continue
                    # R^T R off-diagonal check
                    for a in range(4):
                        for b in range(a + 1, 4):
                            if dot([M[i][a] for i in range(4)], [M[i][b] for i in range(4)]) != 54:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        sols.append(M)
    print("num ordered solutions:", len(sols))
    # canonical representatives under row/col permutations
    seen = set()
    reps = []
    for M in sols:
        key = min(
            tuple(sorted(tuple(M[i][p[j]] for j in range(4)) for i in range(4)))
            for p in itertools.permutations(range(4))
        )
        # note: row order irrelevant -> sort rows; col perms minimized
        if key not in seen:
            seen.add(key)
            reps.append(M)
    print("num classes under row perm + col perm:", len(reps))
    for M in reps:
        for r in M:
            print(r)
        # primitivity: check powers up to 10 for all-positive
        P = [list(r) for r in M]
        prim = None
        for pw in range(1, 11):
            if all(v > 0 for row in P for v in row):
                prim = pw
                break
            P = [[sum(P[i][k] * M[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
        print("primitive exponent:", prim, " min entry:", min(v for row in M for v in row))
        print()
    # headline candidate R = 3J+3I
    Ct = ((6, 3, 3, 3), (3, 6, 3, 3), (3, 3, 6, 3), (3, 3, 3, 6))
    assert any(tuple(M) == Ct for M in sols), "3J+3I must be a solution"
    print("3J+3I verified as valid quotient, all entries >=3 -> primitive exponent 1.")
    # theorem: every entry of every admissible R is >= 2 (row types force it),
    # hence every admissible 9^4 quotient is primitive with exponent 1.

if __name__ == "__main__":
    main()
