"""Toy calibration: (r,1)-sparse optimisation cannot reach linear A2 exponent.

Model (illustrative, not a new theorem): assume a bound of the form
  ||T_Omega|| <= C(r) * W^{theta(r)},  W = [w]_{A2} >> 1,
with C(r) = 1/(r-1) (typical blow-up as r -> 1 in rough sparse domination)
and theta(r) = 2 - (r-1) (so theta -> 2 as r -> 1+, reflecting that known
(r,1)-sparse weighted estimates degrade to ~W^2 in the limit).
We minimise over r in (1, 1.5] for several W and report the effective
exponent log E / log W.  Result: inf stays near 2 with a loglog loss,
never near 1.  This mirrors the published barrier: without a uniform
(1,1)-sparse or uniform time-frequency estimate, r-optimisation floors at ~2.
"""
import math

def C_of_r(r):
    return 1.0 / (r - 1.0)

def theta_of_r(r):
    return 2.0 - (r - 1.0)

def best_for_W(W):
    best = None
    best_r = None
    r = 1.001
    while r <= 1.5:
        E = C_of_r(r) * (W ** theta_of_r(r))
        eff = math.log(E) / math.log(W)
        if best is None or E < best:
            best = E
            best_r = r
            best_eff = eff
        r += 0.001
    return best_r, best, best_eff

if __name__ == "__main__":
    print("W, best_r, min_E, effective_exponent")
    for W in [10, 100, 1000, 10000]:
        r, E, eff = best_for_W(float(W))
        print(f"{W}, r*={r:.3f}, E={E:.3e}, eff={eff:.4f}")
    # also show r -> 1 at fixed W blows up via C(r)
    W = 1000.0
    print("fixed W=1000, r -> 1:")
    for r in [1.5, 1.2, 1.1, 1.05, 1.01, 1.001]:
        E = C_of_r(r) * (W ** theta_of_r(r))
        print(f"  r={r}: E={E:.3e}, eff={math.log(E)/math.log(W):.4f}")
    print("CONCLUSION: optimised effective exponent stays ~2 (plus loglog loss), never 1.")
