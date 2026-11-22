---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof explicitly computes the two projection types, all normal-cone cells, active facets, the opposite-pole incidence, and their common face-to-face fan. This is an all-dimensional proof, not a finite extrapolation. Run `python3 check.py` for exact Fraction vertex comparisons and normal inequalities in 20 cases of dimensions 2 to 6. A separate local SciPy convex-hull volume cross-check passed 16 configurations in dimensions 2 to 5 (finite numerical corroboration only).

No external audit or formal proof was performed. Historical originality is provisional, particularly regarding classical cubical subdivision terminology.
