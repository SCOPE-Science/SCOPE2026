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

# Reproducibility and limits

The proof is analytical and self-contained relative to the published affine vector-field definition. Reproduce the finite supplementary checks with `python3 checker.py` (Python 3 standard library only). The program solves the scalar ray-crossing equation using Newton iteration and independently integrates the original affine sector field in closed form to check that both descriptions yield the same physical ray-intersection points. It verifies zero clock perturbation at the calibration, the unchanged transverse return multiplier, strict positivity of every pairwise sensitivity minor, and finite-difference approximations for all gains in a triangle and irregular five-sided polygon with heterogeneous rates.

Successful executed output ends `All sector-boundary, jet, and strict minor checks passed.` Neither these finitely many tests nor their successful execution establishes an infinite generality claim; that rests on the exact sector integration, Taylor algebra, and strict exponential inequalities in RESULT.md. The section displacement is measured along the ray through the first vertex, not as Euclidean transverse distance. No independent audit has yet been performed.
