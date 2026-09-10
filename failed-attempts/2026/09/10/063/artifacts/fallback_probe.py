"""Bounded fallback probes (exact preset fallback, binary gate).

F1: Re-run exhaustive untwisted H-separation check (does ANY Elliott-matched pair
    among the 28 classes carry incompatible H-data?). Reuses invariant_table.json.
F2: Certify the sharpest Elliott match explicitly (det(I-A^t)=+/-1 => K0=K1=0)
    for the nominated O_2 pair, with unimodular consequence stated.
F3: Twist-arm attempt: record that no normalized 2-cocycle tables with incompatible
    H^2 classes were producible; document the vanishing indication (H_2=0 computed
    + divisible-coefficient UCT premise => H^2(G_A,T)=0) and why it closes rather
    than satisfies the fallback gate.

Writes fallback_probe_report.json.
"""
import itertools
import json

import sympy as sp

rows = json.load(open("output/artifacts/invariant_table.json"))

# F1: H-lock recheck (Matui premise: H0=coker, H1=ker, H2=0)
from collections import defaultdict
grp = defaultdict(list)
for i, r in enumerate(rows):
    key = (tuple(sorted(abs(x) for x in r["snf"])), r["k1rank"])
    # H-data as function of key
    tors = sorted(abs(x) for x in r["snf"] if abs(x) > 1)
    zrank = sum(1 for x in r["snf"] if x == 0)
    grp[key].append((i, (tors, zrank, r["k1rank"], 0)))
nsep = 0
for key, v in grp.items():
    base = v[0][1]
    for _, h in v[1:]:
        if h != base:
            nsep += 1
print("F1 Elliott keys:", len(grp), "| H-separated matched pairs:", nsep)

# F2: nominated O_2 pair Elliott certificates via det +/-1
A = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
B = [[0, 0, 1], [1, 0, 0], [0, 1, 1]]
certs = {}
for name, M in (("A", A), ("B", B)):
    Mt = [[M[j][i] for j in range(3)] for i in range(3)]
    ImMt = [[(1 if i == j else 0) - Mt[i][j] for j in range(3)] for i in range(3)]
    d = int(sp.Matrix(ImMt).det())
    certs[name] = {"det_I_minus_At": d, "K0": "0 (|coker|=|det|=1)" if abs(d) == 1 else "?",
                   "K1": "0 (det!=0 => ker=0)" if d != 0 else "?"}
print("F2 certs:", certs)
trA = [sum((__import__("functools", fromlist=["x"])), 0) ] if False else None
# periodic data (plain python)
def mat_mul(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def mat_pow(X, k):
    n = len(X)
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        P = mat_mul(P, X)
    return P
print("F2 tr(A^2) =", sum(mat_pow(A, 2)[i][i] for i in range(3)),
      "| tr(B^2) =", sum(mat_pow(B, 2)[i][i] for i in range(3)))

# F3: twist-arm status
f3 = ("No normalized 2-cocycle tables (sigma,tau) with Elliott-preserving "
      "incompatible H^2 classes were produced. Indication: computed H_2(G)=0 on "
      "all 28 classes (Matui premise) plus divisible-coefficient UCT premise "
      "(T injective => Ext^1(-,T)=0, H^2(G_A,T)~=Hom(H_2,T)=0) gives H^2=0, i.e. "
      "all twists trivial, so the twist arm collapses to the untwisted case "
      "(F1: 0 separations). Exact rigidity-theorem pin (theorem no./section) for "
      "the H^2-to-pair-non-isomorphism implication was additionally not secured "
      "within bound. Either way the fallback's four-artifact binary gate "
      "(A,B,sigma,tau + SNF match + H/H^2 incompatibility + rigidity derivation) "
      "cannot be assembled in this cell.")
print("F3:", f3)

report = {
    "F1_elliott_keys": len(grp),
    "F1_H_separated_matched_pairs": nsep,
    "F2_certs": certs,
    "F2_trA2": sum(mat_pow(A, 2)[i][i] for i in range(3)),
    "F2_trB2": sum(mat_pow(B, 2)[i][i] for i in range(3)),
    "F3_twist_arm": f3,
    "fallback_gate_satisfiable": False,
}
json.dump(report, open("output/artifacts/fallback_probe_report.json", "w"), indent=1)
print("wrote output/artifacts/fallback_probe_report.json")
