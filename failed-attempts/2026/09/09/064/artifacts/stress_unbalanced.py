"""Stress tests for lane-440 target (balanced + unbalanced admissibility, Stein gaps,
Takahashi P/Q precedent numbers). Unbalanced Euler formula chi = g-(k1+k2+k3)+3p+2b-1
is used as HYPOTHESIS (reduces to Castro-Ozbagci balanced formula when k1=k2=k3=k);
flagged, not asserted as cited."""
import json
from collections import Counter

g, chi = 3, 1
sols = []
for p in range(0, 3):
    for b in range(1, 7):
        for k1 in range(0, 6):
            for k2 in range(0, 6):
                for k3 in range(0, 6):
                    if chi == g - (k1 + k2 + k3) + 3 * p + 2 * b - 1:
                        As = [g + p + b - 1 - k for k in (k1, k2, k3)]
                        if all(0 <= A <= g - p for A in As):
                            sols.append({"p": p, "b": b, "k": [k1, k2, k3]})
dist = dict(sorted(Counter(min(s["k"]) for s in sols).items()))
balanced_334 = {"g": 3, "k": 3, "p": 0, "b": 4,
                "chi_check": 3 - 9 + 0 + 8 - 1,
                "A": 3 + 0 + 4 - 1 - 3}
out = {
    "unbalanced_g3_chi1_count": len(sols),
    "min_ki_distribution": dist,
    "takahashi_type_334_chi": balanced_334,
    "stein_gaps": {"C_base_fr_minus_tb": -2 - (-1), "C_m_fr_minus_tb": 0 - 1},
    "PQ_precedent_chi2": {"unconditional_g_ge": 2 - 1, "conditional_hyp_g_ge": 2 + 2,
                           "diagrams": {"Q": 4, "P": "4-or-5"},
                           "genus_witnesses_exoticness": False},
}
print(json.dumps(out, indent=2))
