#!/usr/bin/env python3
from collections import Counter

def preorder_rows(n):
    diag = sum(1 << (i*n+i) for i in range(n))
    rowmask = (1 << n) - 1
    for bits in range(1 << (n*n)):
        if bits & diag != diag:
            continue
        rows = [(bits >> (i*n)) & rowmask for i in range(n)]
        ok = True
        for i in range(n):
            for j in range(n):
                if ((rows[i] >> j) & 1) and (rows[j] & ~rows[i]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield rows

def is_upset(A, rows):
    return all((rows[x] & ~A) == 0 for x in range(len(rows)) if (A >> x) & 1)

def maximal_core(rows):
    n = len(rows)
    core = 0
    for x in range(n):
        # x is in a maximal equivalence class iff every successor returns to x.
        if all(((rows[y] >> x) & 1) for y in range(n) if (rows[x] >> y) & 1):
            core |= 1 << x
    return core

counts = []
for n in range(1, 5):
    c = 0
    full = (1 << n) - 1
    for rows in preorder_rows(n):
        c += 1
        opens = [A for A in range(1 << n) if is_upset(A, rows)]
        core = maximal_core(rows)
        assert core in opens and core != 0
        dense_opens = []
        for U in opens:
            if U == 0:
                continue
            dense = True
            for O in opens:
                if O != 0 and (O & U) == 0:
                    dense = False
                    break
            if dense:
                dense_opens.append(U)
        assert dense_opens
        assert all((core & ~U) == 0 for U in dense_opens)
        assert core in dense_opens
    counts.append(c)

assert counts == [1, 4, 29, 355]

for n in range(1, 11):
    # Intermediate tail thresholds are 1,...,n-1.
    total = 0
    multiplicity = Counter()
    for mask in range(1 << max(0, n-1)):
        selected = {0, n}
        for i in range(1, n):
            if (mask >> (i-1)) & 1:
                selected.add(i)
        total += 1
        # Least nonempty open has the largest selected threshold < n.
        t = max(i for i in selected if i < n)
        r = n - t
        multiplicity[r] += 1

    assert total == 2 ** max(0, n-1)
    for r in range(1, n+1):
        expected = 1 if r == n else 2 ** (n-r-1)
        assert multiplicity[r] == expected, (n, r, multiplicity[r], expected)

print("PREORDER_COUNTS", counts)
print("VERIFY_OK")
