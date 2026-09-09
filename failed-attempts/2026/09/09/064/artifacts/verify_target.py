"""Auditable checks for lane-440 TARGET phase (no fallback content).

Covers, from cited sources only:
- Gompf tb-minus-1 Stein check (Teng Fig.1 right / Fig.27; family Fig.3/Fig.37;
  criterion: Gompf [9], as used in Takahashi Fig.26: framing = tb - 1).
- Contractible Euler characteristic chi = 1 - 1 + 1 = 1 (Mazur-type handle count).
- Takahashi Thm 1.4 / Cor 4.2 lower-bound functions (conditional, not conclusions).
- Lemma 4.1 admissible (g,k,p,b) enumeration at g=3, chi=1 (balanced case).
- Homeomorphic-pair indistinguishability check: topological bounds coincide
  when chi and boundary topology coincide.
- Binary target pair-test harness: g(Y0)=3 AND g(Y1)>=4 with smooth separation.
"""
import json

# ---- 1. Stein tb-minus-1 checks (Teng pinned fronts) ----
stein_cases = {
    "C_base=C(1,1;-1) [Teng Fig.1 right / Fig.27]": {"framing": -2, "tb": -1},
    "C_m Yasui family [Teng Fig.3 / Fig.37, m>=0 incl. C_1]": {"framing": 0, "tb": 1},
}
stein_results = {}
for name, d in stein_cases.items():
    ok = (d["framing"] == d["tb"] - 1) and (d["framing"] < d["tb"])
    stein_results[name] = ok

# ---- 2. Euler characteristic (Mazur-type: one 0-h, one 1-h, one 2-h) ----
chi = 1 - 1 + 1
assert chi == 1

# ---- 3. Takahashi bounds (functions of hypotheses) ----
def lower_chi_only(c):
    # Thm 1.4(i): g > c - 2  ->  g >= c - 1 (integers)
    return c - 1

def lower_irred_nonseifert(c):
    # Cor 4.2: g > c + 1  ->  g >= c + 2
    return c + 2

def lower_binding(c, b):
    # Thm 1.4(ii) contrapositive direction used for upper?: if no planar
    # open book with b bindings then g > c + b - 2 -> g >= c + b - 1.
    return c + b - 1

b_chi_only = lower_chi_only(chi)          # 0
b_cor42 = lower_irred_nonseifert(chi)     # 3 (CONDITIONAL on boundary incompressibility)
b_b4 = lower_binding(chi, 4)              # 4 (CONDITIONAL on min bindings >= 4)

# ---- 4. Lemma 4.1 enumeration at g=3, chi=1 (balanced) ----
# Constraints: 2p+b-1 <= k <= g+p+b-1 ; chi = g-3k+3p+2b-1 ; A = g+p+b-1-k.
sols = []
g = 3
for p in range(0, 5):
    for b in range(1, 10):
        for k in range(0, 10):
            if not (2 * p + b - 1 <= k <= g + p + b - 1):
                continue
            if g - 3 * k + 3 * p + 2 * b - 1 != chi:
                continue
            A = g + p + b - 1 - k
            # Lemma 4.1 ranges
            if not (0 <= p <= min((g + 1 - chi) / 3, g)):
                continue
            if not ((2 * g - 1 + chi) / 3 <= A <= g - p):
                continue
            sols.append({"k": k, "p": p, "b": b, "A": A})
sols_sorted = sorted(sols, key=lambda d: (d["b"], d["p"], d["k"]))

# ---- 5. Homeomorphic-pair indistinguishability ----
# Same chi + same boundary-topology hypothesis -> same topological lower bound.
pair = {
    "Y0": {"chi": chi, "boundary_hypothesis": "same-as-Y1 (target asserts homeomorphic)"},
    "Y1": {"chi": chi, "boundary_hypothesis": "same-as-Y0 (target asserts homeomorphic)"},
}
topo_bound_Y0 = lower_irred_nonseifert(pair["Y0"]["chi"])
topo_bound_Y1 = lower_irred_nonseifert(pair["Y1"]["chi"])
indistinguishable = (topo_bound_Y0 == topo_bound_Y1)

# ---- 6. Binary target pair-test harness ----
# Evidence flags available in this pass (honest values: no verified diagram,
# no smooth non-existence proof, no boundary hyperbolicity cert for Teng C1).
flags = {
    "verified_genus3_diagram_Y0": False,
    "certified_g_ge_3_Y0": False,   # needs boundary hyperbolicity / binding cert: missing
    "smooth_certified_no_genus3_Y1": False,  # needs smooth obstruction: missing
    "certified_g_ge_4_Y1": False,
}
pair_proved = (
    flags["verified_genus3_diagram_Y0"]
    and flags["certified_g_ge_3_Y0"]
    and flags["smooth_certified_no_genus3_Y1"]
    and flags["certified_g_ge_4_Y1"]
)

report = {
    "stein_tb_minus_1": stein_results,
    "chi": chi,
    "takahashi_bounds_chi1": {
        "chi_only_g_ge": b_chi_only,
        "conditional_irred_nonseifert_g_ge": b_cor42,
        "conditional_min_bindings4_g_ge": b_b4,
        "note": "conditional bounds only; hypotheses unverified for Teng C1/Y1",
    },
    "lemma41_g3_chi1_solutions": sols_sorted,
    "homeomorphic_pair_same_topo_bound": {
        "bound_Y0": topo_bound_Y0, "bound_Y1": topo_bound_Y1,
        "equal": indistinguishable,
    },
    "binary_pair_test": {"flags": flags, "TARGET_PROVED": pair_proved},
}

print(json.dumps(report, indent=2))
print("OVERALL:", "TARGET_PROVED" if pair_proved else "TARGET_NOT_PROVED")
