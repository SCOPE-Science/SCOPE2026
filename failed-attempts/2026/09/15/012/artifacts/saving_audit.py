"""Bounded recovery test: power-saving audit for fixed-weight GL(3) short-window moment.

Compares the TARGET bound against trivial-majorant off-diagonal bounds under
optimistic assumptions (Weil-type Kloosterman saving + Kim-Sarnak-type coefficient
bounds), parametrized by the D-box exponent A (Dmax = T^A). Shows the residual
saving that must come from the missing uniform Kuznetsov-Voronoi archimedean
estimate, and its M-dependence. Pure exponent arithmetic; no external data.
"""
import json
import os

T_EXP_AFE = 1.5        # AFE length N = T^{3/2} (conductor T^3, sqrt)
DIAG_T_EXP = 2.0       # diagonal MT^2 (Plancherel r^2 dr, fixed weight)
THETA_RS = 5.0 / 14.0  # Kim-Sarnak-type exponent toward Ramanujan for GL(3)
PAIR_SUM_EXP = 1.5     # sum_{n1,n2<=N} (n1 n2)^-1/2 ~ N = T^{3/2} (upper bound shape)

def audit(Dmax_exp, kloost_saving_exp_per_Dpair=0.0, coeff_penalty=0.0):
    """Per-pair D-sum exponent + pair-sum exponent vs target exponent 2 (in T).

    Per-pair D-box: #pairs ~ Dmax^2 = T^{2A}; Kloosterman factor per pair
    T^{-s} with s = saving exponent; spectral mass MT^2 common to both sides
    cancels in the comparison, as does M. Returns (offdiag_exp, target_exp, gap).
    """
    dbox = 2.0 * Dmax_exp - kloost_saving_exp_per_Dpair
    offdiag = PAIR_SUM_EXP + dbox + coeff_penalty
    target = DIAG_T_EXP
    return offdiag, target, offdiag - target

rows = []
for A in [0.25, 0.5, 0.75, 1.0, 1.5]:
    # trivial Kloosterman (no saving), no coeff penalty
    o, t, g = audit(A, 0.0, 0.0)
    rows.append({"Dmax_exp": A, "scenario": "trivial Kloosterman",
                 "offdiag_T_exp": round(o, 3), "target_T_exp": t,
                 "gap_T_exp": round(g, 3)})
    # optimistic Weil-type: saves (D1D2)^{1/2} ~ Dmax^1 over the box count
    o, t, g = audit(A, 1.0 * A, 0.0)
    rows.append({"Dmax_exp": A, "scenario": "Weil-type saving",
                 "offdiag_T_exp": round(o, 3), "target_T_exp": t,
                 "gap_T_exp": round(g, 3)})
    # Weil-type + Kim-Sarnak penalty counted adversarially (worst-case coeffs)
    o, t, g = audit(A, 1.0 * A, 2 * THETA_RS * T_EXP_AFE)
    rows.append({"Dmax_exp": A, "scenario": "Weil-type + worst-case coeff penalty",
                 "offdiag_T_exp": round(o, 3), "target_T_exp": t,
                 "gap_T_exp": round(g, 3)})

# M-dependence note: diagonal scales as M^1; trivial off-diagonal majorant also
# scales as M^1 (spectral mass), so the *gap exponent* is M-independent, but the
# *available* archimedean decay weakens as M narrows (uncertainty principle:
# r-localization to width M spreads the Bessel dual transform by ~1/M), so the
# shortest window M = T^theta is the hardest case. Record theta grid.
theta_grid = [0.1, 0.25, 0.5, 0.75]
m_note = ("Gap exponent is M-independent under trivial majorants; feasibility "
          "decreases as theta decreases because narrow-window test functions "
          "widen the dual transform.")

out = {
    "AFE_length_exp": T_EXP_AFE,
    "diagonal_target_exp": DIAG_T_EXP,
    "ramanujan_theta_assumed": round(THETA_RS, 4),
    "rows": rows,
    "theta_grid": theta_grid,
    "m_dependence": m_note,
    "conclusion": ("With no archimedean decay there is no justification for truncating to a small "
                   "D-box: for the realistic untruncated box (A>=0.75) the trivial majorant overshoots "
                   "MT^{2} by >=T^{0.25} even under optimistic Weil-type saving (>=T^{1.3} counting "
                   "worst-case coefficient penalties; >=T^{0.5}/T^{1.5} at A=1.0). The bound would close "
                   "at A<=0.5 only by assuming rapid decay of the fixed-weight (d0=2) Kuznetsov-Voronoi "
                   "composed transform outside that box, uniformly for windows down to T^theta -- "
                   "which is exactly the missing estimate. Short windows (small theta) harden it."),
}

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "saving_audit.json"), "w") as fh:
    json.dump(out, fh, indent=2)

print(json.dumps(out, indent=2))
