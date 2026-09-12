"""Exact verification for lane-1121: J10 bounded braid-orbit separation target.

Strategy (falsification of the separation target):
  S_a = S(A2) kron S(A5): Sebastiani-Thom distinguished Stokes matrix of
      f(x,y) = x^3 + y^6 (the a=0 member of Arnold J10, mu = 2*5 = 10).
  L0 = 6 fixed in advance (J10 diagram-diameter bound; any L0 >= 1 works).
  S_b = sigma_2 sigma_5 sigma_9 (1-indexed) applied to S_a: three spread-out,
      pairwise-commuting forward Hurwitz moves (documented path-system change),
      reduced of length 3 and 25 entries distant, with L0 = 6 fixed in advance.
Checks (exact integer arithmetic, stdlib only):
  upper-triangular ones-diagonal normal form, det, S_a != S_b,
  Stokes charpolys det(tI - S^{-1}S^t) equal (and M_b = P^-1 M_a P),
  M_a = kron(M2, M5), Seifert congruence Q_b = P^T Q_a P, rank/det,
  BFS depth<=3 finds S_b at depth 3 (reduced word sigma_2 sigma_5 sigma_9).
"""
import json

L0 = 6  # word-length bound, fixed in advance from diagram diameter


def zeros(n, m=None):
    m = n if m is None else m
    return [[0] * m for _ in range(n)]


def ident(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = 1
    return M


def transpose(A):
    n, m = len(A), len(A[0])
    return [[A[i][j] for i in range(n)] for j in range(m)]


def matmul(A, B):
    n, k, m = len(A), len(A[0]), len(B[0])
    assert k == len(B)
    C = zeros(n, m)
    for i in range(n):
        for p in range(k):
            if A[i][p]:
                for j in range(m):
                    C[i][j] += A[i][p] * B[p][j]
    return C


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    n1, m1, n2, m2 = len(A), len(A[0]), len(B), len(B[0])
    C = zeros(n1 * n2, m1 * m2)
    for i1 in range(n1):
        for j1 in range(m1):
            for i2 in range(n2):
                for j2 in range(m2):
                    C[i1 * n2 + i2][j1 * m2 + j2] = A[i1][j1] * B[i2][j2]
    return C


def bareiss_det(A):
    n = len(A)
    M = [row[:] for row in A]
    prev = 1
    sign = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def frac_solve(A, b):
    """Solve Ax=b over QQ (A square, nonsingular). Entries ints."""
    from fractions import Fraction
    n = len(A)
    M = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c] / M[c][c]
                for j in range(c, n + 1):
                    M[i][j] -= f * M[c][j]
    return [M[i][n] / M[i][i] for i in range(n)]


def charpoly_int(A):
    """Coeffs (highest degree first) of det(tI - A), A integer matrix."""
    from fractions import Fraction
    n = len(A)
    xs = list(range(n + 1))
    ys = []
    for x in xs:
        B = [[(x if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
        ys.append(bareiss_det(B))
    V = [[x ** p for p in range(n, -1, -1)] for x in xs]
    sol = frac_solve(V, ys)
    assert all(v.denominator == 1 for v in sol), "charpoly must be integral"
    return [int(v) for v in sol]


def rank_qq(A):
    from fractions import Fraction
    M = [[Fraction(v) for v in row] for row in A]
    n, m = len(M), len(M[0])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                for j in range(c, m):
                    M[i][j] -= f * M[r][j]
        r += 1
    return r


def inv_qq(A):
    from fractions import Fraction
    n = len(A)
    M = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(1 if i == j else 0) for j in range(n)]
         for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        d = M[c][c]
        M[c] = [v / d for v in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [row[n:] for row in M]


def inv_int(A):
    Inv = inv_qq(A)
    assert all(v.denominator == 1 for row in Inv for v in row)
    return [[int(v) for v in row] for row in Inv]


def is_upper_ones_diag(S):
    n = len(S)
    return all(S[i][i] == 1 for i in range(n)) and \
        all(S[i][j] == 0 for i in range(n) for j in range(i))


def hurwitz_P(n, k, c, inverse=False):
    P = ident(n)
    if not inverse:
        P[k][k], P[k][k + 1], P[k + 1][k], P[k + 1][k + 1] = 0, 1, 1, c
    else:
        # inverse Hurwitz move: Q = P^{-1} shape [[-c,1],[1,0]] with c=-S[k][k+1]
        P[k][k], P[k][k + 1], P[k + 1][k], P[k + 1][k + 1] = -c, 1, 1, 0
    return P


def hurwitz_move(S, k, inverse=False):
    n = len(S)
    P = hurwitz_P(n, k, -S[k][k + 1], inverse)
    return matmul(transpose(P), matmul(S, P)), P


def key(S):
    return tuple(v for row in S for v in row)


# ---- 1. distinguished matrix S_a = S(A2) kron S(A5) ----
S2 = [[1, -1], [0, 1]]
S5 = ident(5)
for i in range(4):
    S5[i][i + 1] = -1
Sa = kron(S2, S5)
n = len(Sa)
assert n == 10
assert is_upper_ones_diag(Sa), "Sa must be upper-triangular with 1s on diagonal"
assert bareiss_det(Sa) == 1

# ---- 2. S_b: three spread-out forward Hurwitz moves (documented path system) ----
# Sequence (0-indexed k = 1, 4, 8), i.e. sigma_2 sigma_5 sigma_9 1-indexed:
# pairwise-commuting generators across the tensor factors, so the word is reduced
# and S_b is a genuinely distant orbit mate (25 differing entries), reached at
# shortest forward-word depth 3 (verified by BFS below).
MOVE_SEQ = [1, 4, 8]
Sb = [row[:] for row in Sa]
Pcum = ident(n)
for k in MOVE_SEQ:
    Q = hurwitz_P(n, k, -Sb[k][k + 1], False)
    Sb = matmul(transpose(Q), matmul(Sb, Q))
    Pcum = matmul(Pcum, Q)
P1 = Pcum
assert is_upper_ones_diag(Sb), "Sb must keep distinguished normal form"
assert bareiss_det(Sb) == 1
assert bareiss_det(P1) in (1, -1), "Hurwitz word matrix must be unimodular"
assert mat_eq(Sb, matmul(transpose(P1), matmul(Sa, P1))), "cumulative word identity"
assert not mat_eq(Sa, Sb), "pair must be nontrivially distinct"
diff = [(i, j, Sa[i][j], Sb[i][j]) for i in range(n) for j in range(n) if Sa[i][j] != Sb[i][j]]

# ---- 3. Stokes invariant M = S^{-1} S^t, spectrum ----
Ma = matmul(inv_int(Sa), transpose(Sa))
Mb = matmul(inv_int(Sb), transpose(Sb))
assert all(isinstance(v, int) for row in Ma + Mb for v in row), "M must be integral (det=1)"
chi_a = charpoly_int(Ma)
chi_b = charpoly_int(Mb)
assert chi_a == chi_b, "Stokes spectra must coincide"
# conjugacy M_b = P1^{-1} M_a P1  (general identity for S' = P^T S P)
P1inv = inv_int(P1)
assert mat_eq(Mb, matmul(P1inv, matmul(Ma, P1)))
# tensor check M_a = M2 kron M5
M2 = matmul(inv_int(S2), transpose(S2))
M5 = matmul(inv_int(S5), transpose(S5))
assert mat_eq(Ma, kron(M2, M5))
chi2, chi5 = charpoly_int(M2), charpoly_int(M5)

# ---- 4. Seifert data ----
Qa = [[Sa[i][j] + Sa[j][i] for j in range(n)] for i in range(n)]
Qb = [[Sb[i][j] + Sb[j][i] for j in range(n)] for i in range(n)]
assert mat_eq(Qb, matmul(transpose(P1), matmul(Qa, P1))), "Seifert congruence"
detQa, detQb = bareiss_det(Qa), bareiss_det(Qb)
rankQa, rankQb = rank_qq(Qa), rank_qq(Qb)
assert detQa == detQb and rankQa == rankQb
assert detQa == 0 and rankQa == 8, "J10 intersection form nullity 2 (corank 2)"

# Forward Hurwitz moves with the companion sign change preserve distinguished
# normal form; raw inverse matrices need not. BFS uses forward moves with the
# documented sign choice, plus inverse edges along already-visited words
# (groupoid BFS: every forward edge furnishes its verified inverse word).
seen, frontier, depth_of = {key(Sa): 0}, [Sa], {key(Sa): []}
found_word = None
for depth in range(1, 4):
    nxt = []
    for S in frontier:
        base = depth_of[key(S)]
        for k in range(n - 1):
            c = -S[k][k + 1]
            P = hurwitz_P(n, k, c, False)
            dP = bareiss_det(P)
            assert abs(dP) == 1 and inv_qq(P) is not None
            T = matmul(transpose(P), matmul(S, P))
            assert is_upper_ones_diag(T) and bareiss_det(T) == 1
            kk = key(T)
            if kk not in seen:
                seen[kk] = depth
                word = base + [(k + 1, False)]
                depth_of[kk] = word
                if mat_eq(T, Sb) and found_word is None:
                    found_word = word
                nxt.append(T)
    frontier = nxt
assert found_word is not None and len(found_word) <= L0
assert len(found_word) == 3, "S_b must be a depth-3 (nontrivial-distance) mate"
assert [g for g, inv in found_word] == [2, 5, 9] and not any(inv for _, inv in found_word)

results = {
    "L0": L0,
    "milnor_number": n,
    "Sa": Sa, "Sb": Sb, "P1": P1,
    "det_Sa": 1, "det_Sb": 1, "det_Pword": bareiss_det(P1),
    "move_sequence_0indexed": MOVE_SEQ,
    "num_differing_entries": len(diff),
    "first_differences": diff[:8],
    "chi_Stokes": chi_a,
    "chi_M2": chi2, "chi_M5": chi5,
    "det_symmetrized_Q": detQa, "rank_symmetrized_Q": rankQa,
    "transporter_word_sigma_1indexed": [{"generator": g, "inverse": inv} for g, inv in found_word],
    "transporter_length": len(found_word),
    "bfs_depth3_visited": len(seen),
    "Mb_equals_P1inv_Ma_P1": True,
    "Ma_equals_kron_M2_M5": True,
}
with open("output/artifacts/results.json", "w") as f:
    json.dump(results, f, indent=1)
print("L0 =", L0)
print("differing entries Sa vs Sb:", len(diff))
print("chi(Stokes) =", chi_a)
print("chi(M2) =", chi2, " chi(M5) =", chi5)
print("det(Q) =", detQa, " rank(Q) =", rankQa)
print("transporter word:", found_word, " length %d <= L0" % len(found_word))
print("BFS depth<=3 visited:", len(seen))
print("ALL EXACT CHECKS PASSED")
