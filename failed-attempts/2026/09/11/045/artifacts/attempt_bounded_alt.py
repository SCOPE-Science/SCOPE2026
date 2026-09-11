"""Bounded alternative attempt: correctly close the integer-spectrum subfamily?

Necessary-condition audit: for the n=59 cofactor phi (deg 18), the applicable
Greaves-style parity on phi(x-1) is WEAKLY type-2 (2^{i-1} | a_i for i>=1),
NOT full type-2 (a_1 = -223 is fixed odd for every candidate, so full type-2
is vacuous). This script re-tests the exactly-722 integer deviation multisets
(sum d=7, sumsq=65) under the CORRECT weakly-type-2 condition. If survivors
remain, the integer-subfamily exclusion (the bounded partial target) FAILS:
no forbidden-subfamily lemma follows, and the alternative is BLOCKED.

Stdlib + sympy only. Exact integer arithmetic.
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


def coeffs_shifted(roots):
    poly = sp.Poly(1, x)
    for r in roots:
        poly = poly * sp.Poly(x - (r + 1), x)
    return [int(c) for c in poly.all_coeffs()]  # a[0]=1 .. a[18]


def is_weakly_type2(roots):
    a = coeffs_shifted(roots)
    for i in range(1, len(a)):
        if a[i] % (2 ** (i - 1)) != 0:
            return False
    return True


weakly = []
for s in sols:
    roots = [11 + d for d in s]
    # roots in [3,19] by construction, hence > -5 (totally-real + interlacing floor OK)
    assert min(roots) > -5
    if is_weakly_type2(roots):
        weakly.append(tuple(sorted(roots)))

print("weakly-type-2 survivors among integer-root phi:", len(weakly))
for w in weakly:
    print(sorted(w))
if weakly:
    print("RESULT: BLOCKED — integer subfamily NOT excludable by parity/trace filters;")
    print("a per-survivor Jacobi complementary-minor kill is required but unavailable")
    print("in-lane (no Magma/Mathematica/SDP; irrational spectra also uncovered).")
else:
    print("RESULT: integer subfamily excluded.")
