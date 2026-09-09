"""Target-directed narrowing lemma (balanced case): which (g,k,p,b) types can occur
at genus 3 for a contractible side whose boundary is NOT S^3.

Inputs (all cited, all allowed):
- Lemma 4.1 enumeration (Takahashi): balanced g=3, chi=1 -> only 3 types.
- Etnyre-Ozbagci [16] via Takahashi Sec.4: planar open book with b=1 binding
  forces boundary S^3 (lens spaces need b=2).
- Cork-boundary fact: boundary of a (nontrivial, hence infinite-order) cork is
  not S^3. Reason: Diff(S^3) connected (Hatcher) -> every S^3 boundary diffeo
  is isotopic to id -> collar extension gives an extension to any contractible
  filling, contradicting cork non-extension. So dC1 != S^3, and twist sides
  Y0/Y1 share this boundary (twisting does not change boundary).
- Type (k,p,b)=(1,0,1) induces (Lemma 2.2) an open book with page Sigma_{0,1}
  (disk) and 1 binding -> boundary S^3 -> EXCLUDED for Y0/Y1.

Conclusion: any balanced genus-3 relative trisection of Y0 or Y1 is of type
(2,1,1) or (3,0,4). In particular a Y1 genus->=4 proof (balanced) reduces to
ruling out exactly these two types -- but that ruling-out needs smooth input
beyond the cited topological toolkit (flagged, not claimed).
Unbalanced case (Remark 4.3): 21 Euler-admissible g=3 types (hypothesized
formula, flagged); narrowing not carried out there.
"""
import json

# Balanced solutions at g=3, chi=1 (from verify_target.py enumeration)
balanced = [
    {"k": 1, "p": 0, "b": 1, "A": 2},
    {"k": 2, "p": 1, "b": 1, "A": 2},
    {"k": 3, "p": 0, "b": 4, "A": 3},
]
for s in balanced:
    g = 3
    assert s["A"] == g + s["p"] + s["b"] - 1 - s["k"]
    assert g - 3 * s["k"] + 3 * s["p"] + 2 * s["b"] - 1 == 1

# Boundary facts (flags documented honestly: logical deductions, not machine certs)
boundary_is_homology_sphere = True   # contractible + Poincare-Lefschetz
boundary_is_S3 = False               # cork non-extension + Hatcher + collar extension
# (1,0,1): page disk, planar, 1 binding -> S^3 by [16]; contradicts boundary != S^3
excluded_101 = (not boundary_is_S3) and boundary_is_homology_sphere
remaining = [s for s in balanced if not (s["k"] == 1 and s["p"] == 0 and s["b"] == 1 and excluded_101)]

out = {
    "balanced_g3_chi1_types": balanced,
    "boundary_facts": {
        "homology_sphere": boundary_is_homology_sphere,
        "is_S3": boundary_is_S3,
        "why_not_S3": "cork non-extension (f^k never extends) + Diff(S^3) connected [Hatcher] + collar extension",
    },
    "excluded_type_101": excluded_101,
    "remaining_genus3_types": remaining,
    "reading": "Any balanced genus-3 trisection of Y0/Y1 is type (2,1,1) or (3,0,4); "
               "(3,3,0,4) matches the Takahashi Akbulut/Mn precedent type. "
               "Ruling out both types on Y1 needs smooth input: NOT in hand.",
}
print(json.dumps(out, indent=2))
