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

Run `python check.py` with Python 3 and SymPy to reproduce the stationary solution, Jacobian characteristic coefficients and exact rational identities. The checker asserts the cubic discriminant, Descartes sign patterns and all rational root-bracket signs. It prints the two approximate crossing locations only after the exact assertions pass.

The quartic has exactly three positive simple zeros by Descartes' upper bound together with three disjoint intervals of strict sign change; the fourth real zero is strictly negative by the sign variation of \(Q(-t)\). Only the middle and upper positive zeros belong to the coexistence interval. The cubic numerator of \(B\) has negative discriminant and strictly positive value at zero and leading coefficient; it therefore has no positive root. This supplies the analytic sign certificate, independent of floating-point root enumeration.

Reconstruction uses only the model equations as printed and the exact rational rates given in `RESULT.md`. The supplied code is a reproducibility aid, not an independent expert review, and it does not assert nonlinear bifurcation nondegeneracy or exclude uninspected historical priority.
