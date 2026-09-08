"""Exact Hadamard/HT-equivalence decision for 10x10 (+-1)-matrices.

HT-equivalence = signed row permutations + signed column permutations + transpose.
Decision route: dephase (first row/col forced to +1, deterministic), then exact
joint row/column-permutation backtracking, tried with and without transpose.

Backtracking discipline (correctness-critical): the column-extension generator
is fully lazy and self-cleaning -- every assignment it makes is undone when the
generator is resumed or exhausted -- and callers never abandon a live generator
except on the overall-True path (state irrelevant afterwards). Each dfs level
therefore resumes with exactly the state it started with. Pure stdlib.
"""
import sys

sys.setrecursionlimit(100000)


def dephase(M):
    M = [list(map(int, r)) for r in M]
    n = len(M)
    for j in range(n):
        if M[0][j] == -1:
            for i in range(n):
                M[i][j] = -M[i][j]
    for i in range(1, n):
        if M[i][0] == -1:
            for j in range(n):
                M[i][j] = -M[i][j]
    return M


def transpose(M):
    return [list(r) for r in zip(*M)]


def deph_equal(A, B):
    n = len(A) - 1
    a = [row[1:] for row in A[1:]]
    b = [row[1:] for row in B[1:]]
    order = sorted(range(n), key=lambda i: tuple(sorted(a[i])))
    used = [False] * n
    cmap = [-1] * n
    usedc = [False] * n

    def dfs(t):
        if t == n:
            return True
        i = order[t]
        ai = a[i]
        for j in range(n):
            if used[j]:
                continue
            bj = b[j]
            bad = False
            for k in range(n):
                ck = cmap[k]
                if ck != -1 and bj[ck] != ai[k]:
                    bad = True
                    break
            if bad:
                continue
            used[j] = True
            # NOTE: the generator is consumed to exhaustion inside this loop
            # (no early abandon): every extension it yields is tried, and on
            # exhaustion it has undone all its own assignments, restoring the
            # state this level started with.
            for _ in _extend(ai, bj):
                if dfs(t + 1):
                    return True
            used[j] = False
        return False

    def _extend(ai, bj):
        items = [k for k in range(n) if cmap[k] == -1]

        def ncand(k):
            v = ai[k]
            c = 0
            for ell in range(n):
                if not usedc[ell] and bj[ell] == v:
                    c += 1
            return c

        items.sort(key=ncand)

        def rec(s):
            if s == len(items):
                yield
                return
            k = items[s]
            v = ai[k]
            for ell in range(n):
                if not usedc[ell] and bj[ell] == v:
                    cmap[k] = ell
                    usedc[ell] = True
                    yield from rec(s + 1)
                    cmap[k] = -1
                    usedc[ell] = False

        yield from rec(0)

    return dfs(0)


def ht_equal(A0, B0):
    """True iff A0, B0 are HT-equivalent (signed row/col perms + transpose)."""
    for t in (False, True):
        A = dephase(transpose(A0) if t else A0)
        B = dephase(B0)
        if deph_equal(A, B):
            return True
    return False


def bareiss_det(A):
    """Exact integer determinant (fraction-free Bareiss with sign tracking)."""
    n = len(A)
    B = [list(map(int, r)) for r in A]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if B[k][k] == 0:
            piv = next((r for r in range(k + 1, n) if B[r][k] != 0), None)
            if piv is None:
                return 0
            B[k], B[piv] = B[piv], B[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                B[i][j] = (B[i][j] * B[k][k] - B[i][k] * B[k][j]) // prev
            B[i][k] = 0
        prev = B[k][k]
    return sign * B[n - 1][n - 1]
