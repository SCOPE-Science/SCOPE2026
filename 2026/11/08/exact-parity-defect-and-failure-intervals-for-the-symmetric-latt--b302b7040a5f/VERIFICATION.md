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

The claim follows analytically from rank characterization of successive minima, finite Fourier parity enumeration, and elementary rational inequalities. The bundled `verify.py` executes 274 exact tests and independently reconstructs the rank thresholds in low dimensions.

Exact computations use Python's `fractions.Fraction`, including the equality and strict-sign boundary cases. The finite suite tests the formulas but does not prove their all-dimensional validity. The continuous isotropic intervals are proved by the monotonicity of \((2r-1)^n\) on the admissible range and the exact interior counting formula.
