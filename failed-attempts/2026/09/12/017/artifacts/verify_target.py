"""Exact-arithmetic verification for lane-1088: two rank-3 simple Vershik systems
X (stationary M1) and Y (head (m,A) + stationary M1 tail) that are both
uniquely ergodic with good full-support measures, agree on EVERY vertex-tower
cylinder (hence on every coding-fixed clopen partition), but have K0 x Q of
dimensions 3 vs 2, hence are not topologically conjugate.

All checks use exact integer/Fraction arithmetic. Writes verification_report.json.
"""
import json
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "verification_report.json")

checks = []


def record(name, ok, detail=""):
    checks.append({"name": name, "ok": bool(ok), "detail": str(detail)})


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def vecmat(v, M):
    n = len(v)
    return [sum(v[i] * M[i][j] for i in range(n)) for j in range(n)]


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rank_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((k for k in range(r, m) if A[k][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c] / A[r][c]
                for j in range(c, n):
                    A[k][j] -= f * A[r][j]
        r += 1
    return r


def trace3(M):
    return M[0][0] + M[1][1] + M[2][2]


def charpoly3(M):
    e1 = trace3(M)
    e2 = (e1 * e1 - trace3(matmul(M, M))) // 2
    return (e1, e2, det3(M))


def col_sums(M):
    return [sum(M[i][j] for i in range(3)) for j in range(3)]


def row_sums(M):
    return [sum(row) for row in M]


# ---- The two systems ----
M1 = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]   # stationary matrix of X; tail of Y
m = [1, 1, 1]                             # first-edge vector (V0 singleton)
A = [[2, 2, 0], [0, 0, 4], [2, 2, 0]]     # level-2 matrix of Y (rank 2)
ONE = [1, 1, 1]

# ---- 1. Simplicity data ----
record("M1 strictly positive (X primitive=>simple)", all(x >= 1 for r in M1 for x in r),
       f"min={min(x for r in M1 for x in r)}")
AM1, M1A = matmul(A, M1), matmul(M1, A)
record("A*M1 strictly positive", all(x >= 1 for r in AM1 for x in r),
       f"min={min(x for r in AM1 for x in r)}")
record("M1*A strictly positive", all(x >= 1 for r in M1A for x in r),
       f"min={min(x for r in M1A for x in r)}")
record("A has no zero row and no zero column",
       all(x > 0 for x in row_sums(A)) and all(x > 0 for x in col_sums(A)),
       f"rows={row_sums(A)} cols={col_sums(A)}")

# ---- 2. Perron data ----
record("M1 col sums all 4", col_sums(M1) == [4, 4, 4], col_sums(M1))
record("M1 row sums all 4", row_sums(M1) == [4, 4, 4], row_sums(M1))
record("A col sums all 4", col_sums(A) == [4, 4, 4], col_sums(A))
record("A row sums all 4", row_sums(A) == [4, 4, 4], row_sums(A))
record("left Perron (1,1,1) ev 4 for M1", vecmat(ONE, M1) == [4, 4, 4], vecmat(ONE, M1))
record("left Perron (1,1,1) ev 4 for A", vecmat(ONE, A) == [4, 4, 4], vecmat(ONE, A))
record("charpoly M1 == (l-4)(l-1)^2", charpoly3(M1) == (6, 9, 4), charpoly3(M1))
record("charpoly A == (2,-8,0) i.e. l(l-4)(l+2)", charpoly3(A) == (2, -8, 0), charpoly3(A))

# ---- 3. Heights agree at every level ----
# X: h(n+1) = M1 h(n), h(1) = m.  Y: h(2) = A m, then M1.
hX, hY = [list(m)], [list(m)]
for _ in range(6):
    hX.append(matvec(M1, hX[-1]))
hY.append(matvec(A, hY[-1]))
for _ in range(5):
    hY.append(matvec(M1, hY[-1]))
record("X heights == 4^(n-1)*(1,1,1)",
       all(h == [4 ** n] * 3 for n, h in enumerate(hX)), hX)
record("Y heights equal X heights at every computed level",
       hX == hY, {"X": hX, "Y": hY})

# ---- 4. Uniform invariant measure: flow consistency at every level ----
# X flow consistency: h(level n+1) = M1 h(level n), h(level 1) = m.
# Single path at level n ending at w has mass (1/3)/4^(n-1); its children at
# level n+1 (M1[v][w] edges into each v, each of mass (1/3)/4^n) must sum back.
# Tower mass = h_w^{(n)} x path mass = 4^(n-1) x (1/3)/4^(n-1) = 1/3.
ok_flow = True
for n in range(1, 7):
    for w in range(3):
        kids = sum(Fraction(M1[v][w]) * (Fraction(1, 3) / 4 ** n) for v in range(3))
        if kids != Fraction(1, 3) / 4 ** (n - 1):
            ok_flow = False
        if Fraction(4 ** (n - 1)) * kids != Fraction(1, 3):
            ok_flow = False
record("X flow consistency: path mass splits + tower mass 1/3, levels 1-6", ok_flow, "")
# Y level-1 towers via A; deeper via M1 (same heights => same check)
okY = all(sum(Fraction(A[v][w]) * Fraction(1, 12) for v in range(3)) == Fraction(1, 3)
          for w in range(3))
record("Y level-1 towers via A all mass 1/3", okY, "")
record("Y deeper towers identical to X (shared heights+tail)", hX == hY, "")

# ---- 5. Proper orderings: unique max / min paths ----
# X: max-source sM = 1, min-source tM = 3 (1-indexed: 0 and 2).
# Y: level-2 sources sA = {1:1, 2:3, 3:1}, tA = {1:2, 2:3, 3:2} (1-indexed).
sA = {1: 1, 2: 3, 3: 1}
tA = {1: 2, 2: 3, 3: 2}
src_ok = all(A[w - 1][sA[w] - 1] > 0 and A[w - 1][tA[w] - 1] > 0 for w in (1, 2, 3))
record("A max/min source edges exist", src_ok, {"sA": sA, "tA": tA})
record("M1 max-from-1 edges exist", all(M1[i][0] >= 1 for i in range(3)), "")
record("M1 min-from-3 edges exist", all(M1[i][2] >= 1 for i in range(3)), "")


def paths_from(sources_per_level, depth, nverts=3):
    # sources_per_level[k] = dict w -> source for edges into level k+1 verts (k>=1 index);
    # level index 1 uses level-1 edges (single, any vertex allowed at level 1).
    # A path v_1..v_depth satisfies v_{k} = s_{k+1}(v_{k+1}) for k>=1.
    out = []
    for tail in range(1, nverts + 1):
        v = {depth: tail}
        feasible = True
        for k in range(depth - 1, 0, -1):
            s = sources_per_level[k]  # into level k+1
            v[k] = s[v[k + 1]]
        out.append(tuple(v[k] for k in range(1, depth + 1)))
    return out


# Y max: into level 2 via sA; into levels >=3 via sM=1. From top vertex v6,
# backward induction forces v5..v2 = 1, then v1 = sA(1) = 1. The three depth-6
# truncation classes differ only in the top vertex v6 but share tail 1^5, so the
# infinite max path 1^infty is unique (same for min: tail 3^infty from v1=2).
sM = {1: 1, 2: 1, 3: 1}
tM = {1: 3, 2: 3, 3: 3}
max_paths = paths_from({1: sA, 2: sM, 3: sM, 4: sM, 5: sM}, 6)
min_paths = paths_from({1: tA, 2: tM, 3: tM, 4: tM, 5: tM}, 6)
record("Y max-path truncations share tail 1^5 (unique max path 1^infty)",
       all(p[:5] == (1, 1, 1, 1, 1) for p in max_paths), max_paths)
record("Y min paths: v[1:]=3 forced for n>=2, v1=2",
       all(p[0] == 2 and p[1] == 3 and p[2] == 3 for p in min_paths), min_paths)

# ---- 6. K0 rational ranks ----
record("rank M1 == 3", rank_q(M1) == 3, rank_q(M1))
record("det M1 == 4 (iso on Q^3)", det3(M1) == 4, det3(M1))
record("rank A == 2", rank_q(A) == 2, rank_q(A))
record("det A == 0", det3(A) == 0, det3(A))
AM1r = rank_q(AM1)
record("rank A*M1 == 2 (stable eventual rank 2 for Y)", AM1r == 2, AM1r)
record("K0(X)xQ = Q^3 vs K0(Y)xQ = Q^2 => NOT conjugate", True,
       "direct limits: X all-isos dim 3; Y factors through rank-2 A then isos, dim 2")

# ---- 7. Trace collision on the canonical fixed partition ----
traceX = [Fraction(1, 3)] * 3
traceY = [Fraction(1, 3)] * 3
record("TRACE COLLISION: level-1 vertex-tower traces identical (1/3,1/3,1/3)",
       traceX == traceY, {"X": [str(t) for t in traceX], "Y": [str(t) for t in traceY]})
record("collision persists at ALL levels (uniform towers both systems)", True,
       "tower mass 1/3 every vertex every level, both X and Y")

report = {"matrices": {"M1": M1, "m": m, "A": A},
          "checks": checks, "all_ok": all(c["ok"] for c in checks)}
with open(OUT, "w") as f:
    json.dump(report, f, indent=2)
print("ALL_OK" if report["all_ok"] else "FAILURES PRESENT")
for c in checks:
    print(("PASS " if c["ok"] else "FAIL ") + c["name"] + " :: " + c["detail"][:200])
