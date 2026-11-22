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

Run `python3 verify_velocity_cone.py` in a directory containing that embedded file. It uses only the Python standard library and exact `fractions.Fraction` arithmetic. The code enumerates all distinct quadratic pairs of grid zeros for grid sizes 3 through 50, tests each possible cone ray's nodewise sign, checks the proposed sharp formula, checks degree-one endpoints, and constructs nonnegative full-space perturbations outside the exact fixed-basis moment interval. The 1,800 figure is a deterministic weighted count of structural checks, not the number of source-code `assert` statements or a statistical guarantee.

The proof for all sizes is independent of finite enumeration: it relies on the exact classification of extreme rays of the three-dimensional nodally nonnegative quadratic polynomial cone and the uniform limit of a rational maximum over dense midpoint grids. This verification does not assert external or independent mathematical validation.

Scientific limits: fixed real polynomial factors of degree at most two; nonnegative nodal samples; symmetric equispaced nodes; equal mass weights; constant spatial mode present; arbitrary core coefficients. No general time-stepping or optimization-complexity guarantee is made.
