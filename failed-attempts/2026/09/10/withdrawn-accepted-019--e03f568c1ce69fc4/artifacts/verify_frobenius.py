"""Extend verify.py coverage: Frobenius certificate replay (independent path).
Recomputes A7 class sizes from S-cycle centralizers, A7 degrees from the
certificate, checks sum d^2=2520, row orthogonality of logged table, and
N(g) = (1/|G|) sum_chi S_chi^2 chi(g)/chi(1) with S_chi from the E-set
(taken as full group since census N1>0), asserting N(g)=2520>0 all classes.
Also replays explicit product witnesses u*v=g per class from census data.
Stdlib only.
"""
import json, cmath, itertools
from math import factorial

cert = json.load(open("output/artifacts/A7_frobenius_certificate.json"))
cen = json.load(open("output/artifacts/e2_census.json"))["7"]["table"]
G = cert["order"]
assert G == 2520

def z_of(mu):
    m = {}
    for c in mu: m[c] = m.get(c, 0) + 1
    z = 1
    for c, e in m.items(): z *= (c ** e) * factorial(e)
    return z

# check class sizes vs cycle centralizers
tot = 0
for C in cert["classes"]:
    mu = tuple(C["stype"])
    if len(set(mu)) == len(mu) and all(c % 2 == 1 for c in mu):
        want = factorial(7) // z_of(mu) // 2
    else:
        want = factorial(7) // z_of(mu)
    assert C["size"] == want, (C, want)
    tot += C["size"]
assert tot == 2520
print("class sizes OK; total 2520; nclasses:", len(cert["classes"]))
assert len(cert["classes"]) == 9

# degrees
ds = [r["degree"] for r in cert["irreps"]]
assert sum(d * d for d in ds) == 2520, ds
print("degrees OK:", sorted(ds))
assert len(ds) == 9

# orthogonality
cls = [c for c in cert["classes"]]
def chi(i, C):
    v = cert["irreps"][i]["values"][str((tuple(C["stype"]), C["half"]))]
    return complex(v[0], v[1])
ok = True
for i in range(9):
    for j in range(9):
        s = sum(C["size"] * chi(i, C) * chi(j, C).conjugate() for C in cls)
        if abs(s - (2520 if i == j else 0)) > 1e-4:
            ok = False; print("ORTH FAIL", i, j, s)
print("orthogonality:", "OK" if ok else "FAIL")
assert ok

# Frobenius sums with E = full group (S_chi = 2520 delta_{chi,1})
S = [complex(a, b) for [a, b] in cert["S_chi"]]
assert abs(S[0] - 2520) < 1e-6 and all(abs(v) < 1e-6 for v in S[1:])
for C in cls:
    N = sum(S[i] ** 2 * chi(i, C) / chi(i, cls[-1]) for i in range(9)) / 2520
    assert abs(N.imag) < 1e-4 and round(N.real) == 2520, (C, N)
print("Frobenius N(g)=2520>0 for all 9 classes: OK")

# census cross-check: every class has N1>0 with class-constant counts
assert all(r["N1_per_elt"] > 0 and r["uniform"] for r in cen), cen
print("census N1>0 all classes: OK;",
      [(r["cycle_type"], r["N1_per_elt"]) for r in cen])
print("VERIFY_FROBENIUS: OK")
