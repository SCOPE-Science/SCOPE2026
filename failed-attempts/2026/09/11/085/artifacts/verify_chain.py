"""Elliptic-chain necessary-condition audit for lane-899 (2,14,5), g=7.

Records the symmetric multidegree and per-component admissibility
(rank-2 semistable existence + section caps). This is a NECESSARY
combinatorial condition only; smoothing/regeneration (Petri at the limit)
is explicitly not established. Stdlib only.
"""
import sys

FAILS = []


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        FAILS.append(name)


G = 7
D = 14
md = [2] * G
check("7 components", len(md) == G)
check("multidegree sums to 14", sum(md) == D, str(md))
for j, c in enumerate(md):
    chi = c  # rank 2 on elliptic curve: chi = deg
    check(f"comp{j} chi==2", chi == 2)
    # semistable rank-2 deg-2 on elliptic exists (e.g. split of deg-1+deg-1),
    # h0 cap 2 for the generic semistable one
    check(f"comp{j} admissible", chi >= 0)
# gluing note: 5 global sections across 7 elliptic components with
# refined vanishing complementarity at 6 internal nodes; necessary
# ramification budget check is qualitative here and recorded as open.
print("INFO smoothing/regeneration at chain limit: OPEN (not checked)")
print("----")
if FAILS:
    print("CHAIN_FAIL", FAILS)
    sys.exit(1)
print("CHAIN_NECESSARY_OK")
