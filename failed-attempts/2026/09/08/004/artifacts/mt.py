"""Monotone-triangle census for ASM verification (lane-67).

From-scratch backtracking enumeration of monotone triangles with bottom
row (1..n), stream-hashed census, per-height distributions, MT->ASM
bijection check, MRR product, and binomial Gram-determinant certificate
via Bareiss / Fraction-Gaussian / Dodgson condensation.
Stdlib only.
"""

import hashlib
import time
from fractions import Fraction
from math import comb, factorial

# ---------------------------------------------------------------- monotone triangles
# Row k (1-based length k), strictly increasing, values in [1, n].
# Bottom row fixed to (1..n). Interlacing between consecutive rows
# (upper u of length k, lower b of length k+1, 0-based):
#     b[i] <= u[i] <= b[i+1]   for i = 0..k-1.


def gen_mt(n):
    """Yield every monotone triangle of order n as a list of row tuples.

    rows[0] is the top singleton, rows[n-1] the fixed bottom row (1..n).
    """
    if n == 0:
        yield []
        return
    tri = [None] * n
    tri[n - 1] = tuple(range(1, n + 1))

    def rec(k, prev):
        if k == 0:
            yield [tuple(r) for r in tri]
            return
        cur = [0] * k

        def inner(i, lo):
            if i == k:
                tri[k - 1] = tuple(cur)
                yield from rec(k - 1, tuple(cur))
                return
            lo = max(lo, prev[i])
            hi = prev[i + 1]
            for v in range(lo, hi + 1):
                cur[i] = v
                yield from inner(i + 1, v + 1)

        yield from inner(0, prev[0])

    yield from rec(n - 1, tuple(range(1, n + 1)))


def encode_triangle(tri):
    return ";".join(",".join(map(str, row)) for row in tri)


def census(n, hash_stream=True):
    """Count all monotone triangles of order n; sha256 over encoded stream."""
    t0 = time.time()
    h = hashlib.sha256()
    count = 0
    for tri in gen_mt(n):
        count += 1
        if hash_stream:
            h.update((encode_triangle(tri) + "\n").encode())
    return {
        "n": n,
        "count": count,
        "sha256": h.hexdigest() if hash_stream else None,
        "wall_s": time.time() - t0,
    }


def height(tri):
    """Corner-sum / height functional: sum of all entries."""
    return sum(sum(row) for row in tri)


def height_distribution(n):
    """Full {height: multiplicity} table plus extremal witnesses."""
    from collections import Counter
    dist = Counter()
    min_h = max_h = None
    min_t = max_t = None
    count = 0
    for tri in gen_mt(n):
        count += 1
        x = height(tri)
        dist[x] += 1
        if min_h is None or x < min_h:
            min_h, min_t = x, [tuple(r) for r in tri]
        if max_h is None or x > max_h:
            max_h, max_t = x, [tuple(r) for r in tri]
    return {
        "n": n,
        "count": count,
        "dist": dict(sorted(dist.items())),
        "min": min_h,
        "min_witness": min_t,
        "max": max_h,
        "max_witness": max_t,
    }


# ---------------------------------------------------------------- MT -> ASM bijection
# S_1 = bottom row set, ..., S_n = top singleton; B[i][j] = 1{j in S_i};
# A[i][j] = B[i][j]-B[i+1][j] (i<n), A[n][j] = B[n][j].


def mt_to_asm(tri):
    n = len(tri)
    sets = [set(tri[n - i]) for i in range(1, n + 1)]
    B = [[1 if j in sets[i] else 0 for j in range(1, n + 1)]
         for i in range(n)]
    A = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(n):
            A[i][j] = B[i][j] - B[i + 1][j]
    for j in range(n):
        A[n - 1][j] = B[n - 1][j]
    return A


def is_asm(A):
    n = len(A)
    for i in range(n):
        if sum(A[i]) != 1:
            return False
        nz = [x for x in A[i] if x != 0]
        if any(abs(x) != 1 for x in nz):
            return False
        if nz and (nz[0] != 1 or nz[-1] != 1):
            return False
        if any(nz[k] == nz[k + 1] for k in range(len(nz) - 1)):
            return False
    for j in range(n):
        if sum(A[i][j] for i in range(n)) != 1:
            return False
        nz = [A[i][j] for i in range(n) if A[i][j] != 0]
        if any(abs(x) != 1 for x in nz):
            return False
        if nz and (nz[0] != 1 or nz[-1] != 1):
            return False
        if any(nz[k] == nz[k + 1] for k in range(len(nz) - 1)):
            return False
    return True


def bijection_check(n):
    """Every MT maps to a valid ASM; distinct MTs give distinct ASMs."""
    seen = set()
    bad = 0
    count = 0
    for tri in gen_mt(n):
        count += 1
        A = mt_to_asm(tri)
        if not is_asm(A):
            bad += 1
        seen.add(tuple(tuple(r) for r in A))
    return {"n": n, "count": count, "bad": bad,
            "distinct_asms": len(seen), "bijective": bad == 0 and len(seen) == count}


# ---------------------------------------------------------------- MRR product


def mrr(n):
    num = 1
    den = 1
    for k in range(n):
        num *= factorial(3 * k + 1)
        den *= factorial(n + k)
    return num // den


# ---------------------------------------------------------------- binomial determinant
# Pascal matrix L(n)_{i,j} = C(i,j) (0-based, unit lower-triangular, det 1).
# d_k = MRR(k+1)/MRR(k) (telescoping: prod_{k<n} d_k = MRR(n)).
# G(n) = L diag(d) L^T, i.e. G_{i,j} = sum_k C(i,k) C(j,k) d_k.
# Then det G(n) = det(L)^2 prod d_k = MRR(n) by multiplicativity, and every
# leading principal minor is det G(m) = MRR(m) != 0, so fraction-free
# Dodgson condensation never divides by zero on these inputs.


def mrr_ratio(k):
    return Fraction(mrr(k + 1), mrr(k))


def gram_matrix(n):
    d = [mrr_ratio(k) for k in range(n)]
    G = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = Fraction(0)
            for k in range(min(i, j) + 1):
                s += Fraction(comb(i, k) * comb(j, k)) * d[k]
            G[i][j] = s
    return G


def det_bareiss(M):
    """Fraction-free Bareiss elimination, exact, with row-swap signs.

    Accepts integral or rational input: rational inputs are first cleared
    to a common denominator D (det(M) = det(D*M)/D^n), keeping every
    division in the loop exact over integers.
    """
    n = len(M)
    if n == 0:
        return Fraction(1)
    F = [[Fraction(x) for x in row] for row in M]
    from math import gcd
    D = 1
    for row in F:
        for x in row:
            D = D * x.denominator // gcd(D, x.denominator)
    A = [[int(F[i][j] * D) for j in range(n)] for i in range(n)]
    prev = 1
    sign = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return Fraction(0)
            A[k], A[sw] = A[sw], A[k]
            sign *= -1
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
        if prev == 0:
            return Fraction(0)
    return Fraction(sign * A[n - 1][n - 1], D ** n)


def det_fraction_gauss(M):
    """Exact Gaussian elimination over Fraction with partial pivoting."""
    n = len(M)
    if n == 0:
        return Fraction(1)
    A = [[Fraction(x) for x in row] for row in M]
    sign = 1
    for k in range(n):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return Fraction(0)
            A[k], A[sw] = A[sw], A[k]
            sign *= -1
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    d = Fraction(sign)
    for i in range(n):
        d *= A[i][i]
    return d


def det_dodgson(M):
    """Dodgson condensation (Jacobi identity) over exact Fractions.

    Guarded: raises ZeroDivisionError with a documented message if an
    interior (connected-minor) pivot vanishes. On the Gram matrices used
    here every connected minor equals some MRR(m) != 0, so the guard
    never fires (asserted by the caller via leading-minor checks).
    """
    n = len(M)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(M[0][0])
    prev = [[Fraction(1)] * n for _ in range(n)]
    cur = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    size = n
    while size > 1:
        nxt = [[Fraction(0)] * (size - 1) for _ in range(size - 1)]
        for i in range(size - 1):
            for j in range(size - 1):
                piv = Fraction(1) if size == n else prev[i + 1][j + 1]
                if piv == 0:
                    raise ZeroDivisionError(
                        "Dodgson interior pivot vanished at size %d "
                        "position (%d,%d); input needs generic pivoting"
                        % (size, i, j))
                nxt[i][j] = (cur[i][j] * cur[i + 1][j + 1]
                             - cur[i][j + 1] * cur[i + 1][j]) / piv
        prev, cur = cur, nxt
        size -= 1
    return cur[0][0]


def det_dodgson_int(M):
    """Alias kept for API stability; Dodgson is exact over Fractions."""
    return det_dodgson(M)


# ---------------------------------------------------------------- memoized DP counter
# Independent second counting route: states are admissible lower rows;
# F(b) = number of completions of the triangle above row b.
# F(singleton-or-empty base) = 1 and F(b) = sum over valid upper rows u
# of F(u). Memoized on row tuples; cross-checks the backtracker.


def upper_rows(b):
    """All strictly increasing u with b[i] <= u[i] <= b[i+1]."""
    k = len(b) - 1
    if k == 0:
        yield ()
        return
    cur = [0] * k

    def inner(i, lo):
        if i == k:
            yield tuple(cur)
            return
        for v in range(max(lo, b[i]), b[i + 1] + 1):
            cur[i] = v
            yield from inner(i + 1, v + 1)

    yield from inner(0, b[0])


def count_dp(n, _memo=None):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def F(b):
        if len(b) <= 1:
            return 1
        return sum(F(u) for u in upper_rows(b))

    return F(tuple(range(1, n + 1))) if n else 1
