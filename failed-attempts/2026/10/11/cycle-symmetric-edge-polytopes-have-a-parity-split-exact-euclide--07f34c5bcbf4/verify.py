#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

def facet_walks(n):
    if n % 2 == 0:
        k = n // 2
        for plus in combinations(range(n), k):
            steps = [-1] * n
            for i in plus:
                steps[i] = 1
            vals = [0]
            for i in range(n - 1):
                vals.append(vals[-1] + steps[i])
            assert vals[-1] + steps[-1] == 0
            yield steps, vals
    else:
        k = (n - 1) // 2
        for zero in range(n):
            remaining = [i for i in range(n) if i != zero]
            for plus in combinations(remaining, k):
                steps = [-1] * n
                steps[zero] = 0
                for i in plus:
                    steps[i] = 1
                vals = [0]
                for i in range(n - 1):
                    vals.append(vals[-1] + steps[i])
                assert vals[-1] + steps[-1] == 0
                yield steps, vals

def centered(vals):
    n = len(vals)
    mean = Fraction(sum(vals), n)
    return [Fraction(v) - mean for v in vals]

def norm2(vals):
    return sum(x*x for x in centered(vals))

def rank_fraction(rows):
    if not rows:
        return 0
    A = [list(map(Fraction, row)) for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q*A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def predicted_norm2(n):
    if n % 2 == 0:
        return Fraction(n * (n*n + 8), 48)
    return Fraction((n*n - 1) * (n*n + 3), 48*n)

rows = []
for n in range(3, 15):
    expected_total = comb(n, n//2) if n % 2 == 0 else n * comb(n-1, (n-1)//2)
    mx = Fraction(-1)
    tangents = []
    total = 0
    for steps, vals in facet_walks(n):
        total += 1
        q = norm2(vals)
        if q > mx:
            mx = q
            tangents = [centered(vals)]
        elif q == mx:
            tangents.append(centered(vals))

    assert total == expected_total, (n, total, expected_total)
    assert mx == predicted_norm2(n), (n, mx, predicted_norm2(n))
    expected_tangent = n if n % 2 == 0 else 2*n
    assert len(tangents) == expected_tangent, (n, len(tangents), expected_tangent)

    rr = rank_fraction(tangents)
    if n % 2:
        assert rr == n - 1, (n, rr)
    else:
        k = n // 2
        assert rr == k, (n, rr)
        # The orthogonal complement inside sum-zero space is exactly the
        # k-periodic subspace. Check a basis of that subspace.
        for j in range(k - 1):
            v = [Fraction(0) for _ in range(n)]
            v[j] = 1
            v[k-1] = -1
            v[j+k] = 1
            v[2*k-1] = -1
            for g in tangents:
                assert sum(a*b for a,b in zip(v,g)) == 0

    rows.append((n, total, len(tangents), str(mx), rr))

print("VERIFY_OK cycle-symmetric-edge-inradius n=3..14 exact_facets=yes exact_rank=yes")
for row in rows:
    print("n=%d facets=%d tangent=%d max_norm2=%s tangent_rank=%d" % row)
