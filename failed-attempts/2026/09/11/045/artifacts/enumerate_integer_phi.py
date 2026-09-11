"""Replay: integer-spectrum slice of the n=59 Seidel family in rank 18.

Derivation (see WORKLOG): for a 59-line angle-1/5 system in R^18, the Seidel
matrix S (0 diag, +-1 off) has Char_S = (x+5)^41 * phi with deg phi = 18,
sum(roots) = 205, sum(roots^2) = 2397 (from tr S = 0, tr S^2 = 59*58).
With d_i = root_i - 11: sum d = 7, sum d^2 = 65.

This script:
  1. exhaustively enumerates nondecreasing deviation multisets in [-8,8]^18
     with sum 7 and sumsq 65 (exact count),
  2. tests the Greaves type-2 necessary condition on phi(x-1)
     (2^i divides coefficient a_i for all i) with sympy exact arithmetic.

Stdlib + sympy only.
"""
import sys
import sympy as sp

sys.setrecursionlimit(100000)

TARGET_SUM = 7
TARGET_SQ = 65
N = 18
LO, HI = -8, 8

sols = []


def dfs(pos, ssum, ssq, cur, lo):
    if pos == N:
        if ssum == TARGET_SUM and ssq == TARGET_SQ:
            sols.append(tuple(cur))
        return
    rem_after = N - pos - 1
    for d in range(lo, HI + 1):
        ns = ssum + d
        nq = ssq + d * d
        if nq > TARGET_SQ:
            if d >= 0:
                break
            continue
        if ns + rem_after * d > TARGET_SUM:
            break
        if ns + rem_after * HI < TARGET_SUM:
            continue
        cur.append(d)
        dfs(pos + 1, ns, nq, cur, d)
        cur.pop()


dfs(0, 0, 0, [], LO)
print("integer-root deviation multisets:", len(sols))
assert len(sols) == 722, len(sols)

x = sp.Symbol("x")


def is_type2(roots):
    poly = sp.Poly(1, x)
    for r in roots:
        poly = poly * sp.Poly(x - (r + 1), x)
    a = [int(c) for c in poly.all_coeffs()]  # a[0]=1 .. a[18]
    for i, ai in enumerate(a):
        if ai % (2 ** i) != 0:
            return False
    return True


surv = [tuple(11 + d for d in s) for s in sols if is_type2([11 + d for d in s])]
print("type-2 survivors among integer-root phi:", len(surv))
assert len(surv) == 0
print("RESULT: 722 integer-root families enumerated, 0 satisfy type-2.")
print("Integer-spectrum subcase is empty; irrational spectra NOT covered.")
