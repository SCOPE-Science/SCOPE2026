"""Recovery test: is there ANY Elliott-matched primitive 3x3 pair with incompatible H-data?

Uses Matui's SFT-groupoid homology formulas (published theorem, stated here as the
test's premise):
  H_0(G_A) = coker(I - A^t)   (= K_0(O_A), Bowen-Franks group)
  H_1(G_A) = ker(I - A^t)     (= K_1(O_A))
  H_n(G_A) = 0 for n >= 2     (in particular H_2 = 0 identically on this cell)
Elliott key for the test: (abs-SNF diag of I-A^t, K1 rank). For the trivial-group
subfamily (K0=0, K1=0) the unit class [1]=0 automatically, so the key is the FULL
unital Elliott invariant and every pair in it satisfies target clause (i) with C=O_2.

The test checks every Elliott-matched pair among the 28 permutation classes for
H-incompatibility. Result: none exists, by construction (H-data is a function of
the Elliott key). Nominates the sharpest explicit O_2 pair as evidence.
"""
import itertools
import json

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_pow(A, k):
    n = len(A)
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        P = mat_mul(P, A)
    return P


def primitivity_power(A):
    for m in range(1, 6):
        if all(v > 0 for row in mat_pow(A, m) for v in row):
            return m
    return None


PERMS = list(itertools.permutations([0, 1, 2]))


def canon(A):
    return min(tuple(A[p[i]][p[j]] for i in range(3) for j in range(3)) for p in PERMS)


mats = []
for bits in itertools.product([0, 1], repeat=9):
    A = [list(bits[i * 3:(i + 1) * 3]) for i in range(3)]
    if primitivity_power(A) is not None:
        mats.append(A)
classes = {}
for A in mats:
    classes.setdefault(canon(A), A)
reps = [classes[c] for c in sorted(classes)]

rows = []
for A in reps:
    At = [[A[j][i] for j in range(3)] for i in range(3)]
    ImAt = [[(1 if i == j else 0) - At[i][j] for j in range(3)] for i in range(3)]
    D = smith_normal_form(sp.Matrix(ImAt))
    d = tuple(sorted(abs(int(D[i, i])) for i in range(3)))
    det = int(sp.Matrix(ImAt).det())
    k1 = sum(1 for x in d if x == 0)
    # H-data under Matui premise (additive notation for H_0)
    h0 = [x for x in d if x > 1]  # finite cyclic summands; zeros -> Z summands
    zrank = sum(1 for x in d if x == 0)
    tr = [sum(mat_pow(A, k)[i][i] for i in range(3)) for k in (1, 2, 3)]
    rows.append({"A": A, "abs_snf": list(d), "det": det, "k1rank": k1,
                 "H0_tors": h0, "H0_Zrank": zrank, "H1_Zrank": k1, "H2": 0,
                 "tr": tr, "prim_pow": primitivity_power(A)})

from collections import defaultdict
grp = defaultdict(list)
for i, r in enumerate(rows):
    grp[(tuple(r["abs_snf"]), r["k1rank"])].append(i)

print("classes:", len(rows), "| Elliott keys:", len(grp))
nsep = 0
for key in sorted(grp):
    idx = grp[key]
    base = rows[idx[0]]
    for j in idx[1:]:
        r = rows[j]
        if (r["H0_tors"], r["H0_Zrank"], r["H1_Zrank"], r["H2"]) != \
           (base["H0_tors"], base["H0_Zrank"], base["H1_Zrank"], base["H2"]):
            nsep += 1
            print("SEPARATED:", key, base["A"], r["A"])
print("Elliott-matched pairs with incompatible H-data:", nsep)

o2 = [i for i, r in enumerate(rows) if r["abs_snf"] == [1, 1, 1] and r["k1rank"] == 0]
print("trivial-Elliott (O_2) class count:", len(o2))
for i in o2:
    print("  O2-member:", rows[i]["A"], "det=", rows[i]["det"],
          "tr=", rows[i]["tr"], "prim_pow=", rows[i]["prim_pow"])

# Nominated sharpest pair: same Elliott (trivial), most different periodic data
a = rows[o2[0]]
b = max((rows[i] for i in o2[1:]), key=lambda r: abs(r["tr"][1] - a["tr"][1]))
print("NOMINATED PAIR:")
print("  A =", a["A"], "tr =", a["tr"])
print("  B =", b["A"], "tr =", b["tr"])
print("  Elliott: K0=0, K1=0, [1]=0 both -> O_A ~= O_B ~= O_2 (Kirchberg-Phillips).")
print("  H-data both: H0=0, H1=0, H2=0 -> COMPATIBLE (no H-separation).")

with open("output/artifacts/recovery_report.json", "w") as f:
    json.dump({"n_classes": len(rows), "n_keys": len(grp),
               "n_H_separated_pairs": nsep,
               "n_O2_members": len(o2),
               "nominated": {"A": a["A"], "B": b["A"]}}, f, indent=1)
print("wrote output/artifacts/recovery_report.json")
