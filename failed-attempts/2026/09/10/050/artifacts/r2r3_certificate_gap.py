"""Route R2/R3 recovery arithmetic: certificate requirements vs available bounds.

Target: delta0=1e-5, C=20 => radius coeff R = C*sqrt(delta0) = 0.0632456.
F = Theta_{4,4,4}: 2 endpoints + 3 paths x 3 internal vertices = 11 vertices,
3 paths x 4 edges = 12 edges.
Checks:
 (a) radius/window arithmetic: A_n must lie within (R+delta0) n^{5/4} of ex;
 (b) F parameters for container hypergraph setup (v=11, e=12);
 (c) D4 density constant from R1 for scale reference.
stdlib only; writes r2r3_certificate_gap.json.
"""
import json
import math

delta0 = 1e-5
C = 20
R = C * math.sqrt(delta0)
window = R + delta0

# F = Theta_{4,4,4} parameters
vF = 2 + 3 * 3
eF = 3 * 4

# D4 scale reference from R1 output
d4_const = 243 / (162 ** 1.25)

out = {
    "delta0": delta0,
    "C": C,
    "radius_coeff_R": R,
    "window_coeff_R_plus_delta0": window,
    "F_vertices": vF,
    "F_edges": eF,
    "D4_E_over_N54_q3": d4_const,
    "container_block": (
        "Balanced-supersaturation lemma for Theta_{4,4,4} (v=11,e=12) with "
        "explicit constants is not in Liu-Yang/Faudree-Simonovits (upper bounds "
        "only, no container fingerprints, no explicit K). No explicit K can be "
        "extracted without a new supersaturation count."
    ),
    "spectral_block": (
        "Uniform eigenvalue gap gamma>0 over ALL F-free near-extremals is "
        "unpublished; degree-sequence interlacing alone cannot distinguish "
        "non-isomorphic same-degree-sequence graphs at edit distance "
        ">> R n^{5/4}. Expander-mixing conversion needs a uniform lambda bound "
        "that is not available for this family."
    ),
    "window_block": (
        "Stability with radius 0.06325 n^{5/4} requires the true extremal number "
        "to lie within 0.06326 n^{5/4} of e(A_n); no published upper bound pins "
        "ex(n,F)/n^{5/4} that tightly (Faudree-Simonovits/Liu-Yang constants are "
        "O(1) and large, lower constants small). Proving the needed upper-bound "
        "sharpening is itself a major open improvement, not an hour-scale lemma."
    ),
}
with open("r2r3_certificate_gap.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
