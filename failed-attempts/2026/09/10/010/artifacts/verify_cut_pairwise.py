"""Pairwise cut-contradiction (the exact ICT condition for phi1, no indiscernibility assumed).
For ANY array (b_i)_{i<w} (w>=2) in a linear order, phi1(x;y):=(y<x) cannot satisfy
Kaplan-et-al Def 2.4(iii): Gamma_{eta} with eta(1)=0 needs b_0<x /\\ x<=b_1
  => b_0<b_1; Gamma_{nu} with nu(1)=1 needs b_1<x /\\ x<=b_0 => b_1<b_0. Contradiction.
Equal case b_0=b_1: single Gamma needs b<x /\\ x<=b, inconsistent.
Exhaustive check over all weak order types on {b0,b1}: each type kills at least one Gamma.
"""
import itertools

def holds(b0, b1, picks):
    """picks: dict eta_value -> 'exists c with b_eta<c<=b_other' feasibility over rationals."""
    feas = {}
    for eta in [0, 1]:
        lo = (b0 if eta == 0 else b1)
        hi = (b1 if eta == 0 else b0)
        feas[eta] = (lo < hi)  # exists rational c with lo<c<=hi iff lo<hi
    return feas

killed = 0
total = 0
for b0, b1 in itertools.product([0, 1, 2], repeat=2):
    total += 1
    f = holds(b0, b1, None)
    # ICT needs BOTH feasible; show at least one fails OR both imply b0<b1 & b1<b0
    if not (f[0] and f[1]):
        killed += 1
        status = f"fails: eta=0 feas={f[0]}, eta=1 feas={f[1]}"
    else:
        # both feasible => b0<b1 and b1<b0 simultaneously: impossible since b's fixed
        # (this branch never happens for fixed b0,b1: f0=(b0<b1), f1=(b1<b0))
        status = "BOTH feasible (implies b0<b1<b0)"
    print(f"(b0,b1)=({b0},{b1}): {status}")
print(f"order-types: {total}, at least one Gamma infeasible: {killed}")
assert killed == total, "for fixed params both Gamma can never be simultaneously feasible"
print("PAIRWISE_CUT_CONTRADICTION_OK")
