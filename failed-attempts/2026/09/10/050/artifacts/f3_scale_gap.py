"""Fallback attempt F3: density-scale arithmetic showing the known explicit /
probabilistic routes cannot reach 1e-6 n^{5/4} for arbitrarily large n.

- Random alteration for F=Theta_{4,4,4} (v=11,e=12): e ~ c n^{2-(v-2)/(e-1)}
  = c n^{13/11} (exponent 13/11 = 1.1818 < 5/4). Ratio to threshold -> 0.
- Lazebnik-Ustimenko-type C8-free explicit: O(n^{6/5}) (exponent 1.2 < 1.25).
  (C8-free => F-free since F contains C8, but too sparse asymptotically;
  Conlon even conjectures ex(n,C8) = o(n^{5/4}).)
- Fixed-direction-restricted D4: Theta(n^{3/4}).
- Disjoint union of fixed F-free base H: Theta(n).
Each meets 1e-6 n^{5/4} only for bounded n; "infinitely many (unbounded) n"
needs true exponent 5/4, for which no explicit F-free family is published.
stdlib only.
"""
import json

thr = 1e-6
routes = {
    "random_alteration_n1311": 13 / 11,
    "LU_C8free_n65": 6 / 5,
    "dir_restricted_D4_n34": 3 / 4,
    "disjoint_union_fixed_base_n1": 1.0,
}
target_exp = 5 / 4
out = {}
for name, exp in routes.items():
    gap = target_exp - exp
    # e = 1 * n^exp >= 1e-6 n^{5/4}  <=>  n^gap <= 1e6  <=>  n <= 1e6^{1/gap}
    nmax = 1e6 ** (1 / gap) if gap > 0 else float("inf")
    out[name] = {"exponent": exp, "gap_to_54": gap,
                 "nmax_with_unit_constant": nmax}
    print(name, out[name])
with open("f3_scale_gap.json", "w") as f:
    json.dump({"target_exponent": target_exp, "routes": out}, f, indent=2)
print("wrote f3_scale_gap.json")
