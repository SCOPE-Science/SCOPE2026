"""Exact-rational verification for lane-123 partial theorem.

Stdlib only (math.comb, fractions.Fraction). Verifies:
 (G) Griesmer numbers G(k,d) for the (48,12) cascade and residual strata.
 (K) Krawtchouk matrix implementation validated on Hamming [7,4,3].
 (P) Pless/moment identities j=0,1,2 for putative [48,12,18] + explicit
     order-2 feasible rational distribution (LP-weakness witness).
 (R) Residual construction pipeline validated on Hamming [7,4,3]:
     min-weight word -> [4,3,>=2] residual with dim exactly k-1.
 (I) Intersection arithmetic: two weight-18 words overlap in <=9 positions
     (exact integer check of the lifting inequalities).

Writes results.json. Exits nonzero on any failure.
"""
import json
import math
import os
from fractions import Fraction

C = math.comb
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
results = {}


def griesmer(k, d):
    return sum((d + (1 << i) - 1) // (1 << i) for i in range(k))


# ---- (G) Griesmer numbers ----
G = {
    "G(12,18)": griesmer(12, 18),
    "G(12,19)": griesmer(12, 19),
    "G(12,17)": griesmer(12, 17),
    "G(11,9)": griesmer(11, 9),
    "G(11,10)": griesmer(11, 10),
    "G(11,11)": griesmer(11, 11),
}
assert G["G(12,18)"] == 44, G
assert G["G(12,19)"] == 46, G
assert G["G(11,9)"] == 26, G
assert G["G(11,10)"] == 27, G
# cascade checks
assert 48 >= G["G(12,18)"]  # Griesmer does not kill [48,12,18]
assert 48 >= G["G(12,19)"]  # nor [48,12,19]; need residual cascade
assert 30 >= G["G(11,10)"] and 30 >= G["G(11,9)"]  # residual strata allowed
results["griesmer"] = G


# ---- (K) Krawtchouk ----
def krawtchouk(j, i, n):
    return sum(((-1) ** t) * C(i, t) * C(n - i, j - t)
               for t in range(max(0, j - (n - i)), min(i, j) + 1))


def dual_dist(A, n, M):
    """A: dict weight->count; M=|C|. Returns dict j->Fraction B_j."""
    B = {}
    for j in range(n + 1):
        B[j] = sum(Fraction(cnt) * krawtchouk(j, i, n)
                   for i, cnt in A.items()) / M
    return B


# Validate on Hamming [7,4,3]: dual is the simplex [7,3,4], B={0:1,4:7}.
A_ham = {0: 1, 3: 7, 4: 7, 7: 1}
B_simplex = {0: 1, 4: 7}
B_ham = dual_dist(A_ham, 7, 16)
assert all(B_ham[j] == B_simplex.get(j, 0) for j in range(8)), \
    {j: B_ham[j] for j in range(8)}
assert sum(B_ham.values()) == 2 ** (7 - 4) * 1  # sum B = 2^{n-k}
results["krawtchouk_hamming_check"] = "pass"


def moment_poly_check():
    """Verify closed forms sum_i C(i,t parities) by brute force at n=48.

    We verify the identities used in the DRAFT:
      K_0(i) = 1
      K_1(i) = n - 2i
      sum over putative enumerator gives B_1 = n - S1*2/M ... etc.
    by direct evaluation on the order-2 witness below.
    """
    n = 48
    for i in [0, 18, 24, 30, 48]:
        assert krawtchouk(0, i, n) == 1
        assert krawtchouk(1, i, n) == n - 2 * i
        # K_2(i) = 2i^2 - 2ni + n(n-1)/2
        assert krawtchouk(2, i, n) == 2 * i * i - 2 * n * i + n * (n - 1) // 2
    return "pass"


results["moment_poly_check"] = moment_poly_check()

# ---- (P) putative [48,12,18] order <=2 moments + LP-weakness witness ----
# With B1 = z (zero coords), M = 4096:
#   S1 = sum i A_i = 2^{k-1} (n - z)
#   S2 = sum i^2 A_i = 2^{k-2} ((n-z)(n-z+1) + 2*B2 - ... )
# We use the Krawtchouk route directly (no quoted formula): with z=0,
#   B1 = (1/M) sum A_i (n-2i) = 0  <=> S1 = M n/2
#   B2 = (1/M) sum A_i K_2(i) = 0  <=> S2 fixed.
n, M = 48, 4096
S1_target = M * n // 2  # 98304
assert S1_target == 98304
# K_2 sum target for B2=0: sum A_i K_2(i) = 0
# Witness support {18,24,30}: a=2018/3, b=8237/3, c=2030/3 (plus A0=1).
a, b, c = Fraction(2018, 3), Fraction(8237, 3), Fraction(2030, 3)
A_wit = {0: Fraction(1), 18: a, 24: b, 30: c}
assert sum(A_wit.values()) == M
S1 = sum(Fraction(i) * cnt for i, cnt in A_wit.items())
assert S1 == S1_target, S1
B1 = sum(cnt * krawtchouk(1, i, n) for i, cnt in A_wit.items()) / M
assert B1 == 0, B1
B2 = sum(cnt * krawtchouk(2, i, n) for i, cnt in A_wit.items()) / M
assert B2 == 0, B2
S2 = sum(Fraction(i * i) * cnt for i, cnt in A_wit.items())
assert S2 == Fraction(2408448), S2
# All witness masses strictly positive rationals, support min weight 18.
assert a > 0 and b > 0 and c > 0
# Dual sum check for the formal distribution: sum B not needed (only j<=2
# constrained); record B_0..B_2.
results["order2_witness"] = {
    "A0": "1", "A18": "2018/3", "A24": "8237/3", "A30": "2030/3",
    "S1": str(S1), "S2": str(S2), "B1": str(B1), "B2": str(B2),
    "conclusion": ("Nonnegative rational formal distribution with min weight 18 "
                   "satisfies MacWilliams j=0,1,2 with B1=B2=0; hence "
                   "second-order moments alone cannot rule out [48,12,18]."),
}

# Degenerate-coordinate bound: zero coords z satisfy 48-z >= G(12,18)=44.
degen = {z: 48 - z >= G["G(12,18)"] for z in range(7)}
assert degen[0] and degen[4] and not degen[5]
results["degenerate_bound"] = {"max_zero_coords": 4}


# ---- (R) residual pipeline on Hamming [7,4,3] ----
def hamming_74():
    """Return list of 16 codewords (7-tuples) of Hamming [7,4,3]."""
    # Parity-check columns = nonzero binary triples; generator: systematic.
    Gmat = [
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
    ]
    words = []
    for m in range(16):
        w = [0] * 7
        for r in range(4):
            if (m >> r) & 1:
                w = [(x + y) % 2 for x, y in zip(w, Gmat[r])]
        words.append(tuple(w))
    return words


def residual_params(words, c, n):
    """Res(C;c): puncture support of c, project all words. Returns (length, dim, mindist)."""
    supp = [j for j in range(n) if c[j] == 1]
    rest = [j for j in range(n) if c[j] == 0]
    proj = set(tuple(w[j] for j in rest) for w in words)
    # dimension over GF(2)
    basis = []
    for v in proj:
        x = list(v)
        for b in basis:
            # eliminate leading one
            piv = next((t for t in range(len(x)) if b[t] == 1), None)
            if piv is not None and x[piv] == 1:
                x = [(u + vv) % 2 for u, vv in zip(x, b)]
        piv = next((t for t in range(len(x)) if x[t] == 1), None)
        if piv is not None:
            basis.append(x)
    dim = len(basis)
    nz = [sum(v) for v in proj]
    mindist = min(w for w in nz if w > 0)
    return len(rest), dim, mindist


words = hamming_74()
dmin = min(sum(w) for w in words if sum(w) > 0)
assert dmin == 3
c = next(w for w in words if sum(w) == 3)
ln, dm, dd = residual_params(words, c, 7)
assert (ln, dm) == (4, 3), (ln, dm)
assert dd >= (3 + 1) // 2, dd  # residual bound ceil(d/2)
results["residual_pipeline_hamming"] = {
    "parent": "[7,4,3]", "residual_length": ln,
    "residual_dim": dm, "residual_mindist": dd,
    "bound_ceil_d_over_2": 2, "status": "pass",
}

# ---- (I) intersection arithmetic for two weight-18 words ----
# x weight 18, overlap s with supp(c): projection weight v=18-s must be 0 or >=9;
# second preimage weight 36-2s must be 0 or >=18. Both force s<=9 (s=18 <-> x=c).
ok = [s for s in range(19)
      if ((18 - s == 0 or 18 - s >= 9) and (36 - 2 * s == 0 or 36 - 2 * s >= 18))]
assert ok == list(range(10)) + [18], ok
results["intersection_bound"] = {"allowed_overlaps": ok, "max_s_distinct": 9}

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)
print("ALL EXACT CHECKS PASS")
print(json.dumps(results, indent=2))
