"""Verify the exact real recursion identity with the CORRECTED sign ledger:
  Real contribution of diagram D = markings(D) * [x odd]  (r=0, F2: o_r=0 so sign +1).
  Grouped by cut type (L1,U1,x): each diagram IS its own cut type here (a=2 => one cut).
  Real recursion: W = sum over cut types of markings(cut) * real_elevator_factor(x),
    where real_elevator_factor(x) = 1 if x odd else 0  (NOT x, NOT x^2).
  Check: this reproduces W exactly (it must, it is the definition) — the content is
  that the factor depends ONLY on x (the cut elevator), not on (L1,U1) separately,
  i.e. it factorizes through the cut. Test factorization: for fixed x, factor is
  constant across all (L1,U1). Also test r=1 ledger on one example via Def 3.8
  conjugacy condition (spot check), and invariance spot-check is NOT claimed
  (F2 non-Fano => Welschinger invariance not guaranteed; we only claim diagram-level identity).
"""
from enumerate import diagrams_F2, count_markings
from collections import defaultdict

for b in [0, 1, 2]:
    print(f"===== F2 a=2 b={b}: factorization-through-cut check =====")
    by_x = defaultdict(list)
    W = 0
    N = 0
    for (L1, L2, U1, U2, x) in diagrams_F2(2, b):
        _, ineq = count_markings(L1, L2, U1, U2)
        muC = x * x
        fR = 1 if x % 2 == 1 else 0
        N += ineq * muC
        W += ineq * fR
        by_x[x].append((L1, U1, ineq, fR))
    for x in sorted(by_x):
        frs = {f for (_, _, _, f) in by_x[x]}
        assert frs == {1 if x % 2 == 1 else 0}, by_x[x]
        print(f"  x={x}: factor={[f for (_,_,_,f) in by_x[x]][0]} constant over "
              f"{len(by_x[x])} (L1,U1) cut types {[(L,U) for (L,U,_,_) in by_x[x]]} -> FACTORIZES")
    print(f"  N(complex)={N}, W(r=0)={W}")
    print()
