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

The analytic argument reduces the nonlinear projection's global seminorm to the largest weighted-variation column norm among all locally realizable contiguous-block averaging matrices, and identifies those norms with the upper concave envelope.

The standalone supplementary checker is `verify.py`; run `python verify.py` using Python 3. It executes exact rational contiguous-partition comparisons, exact pooled-block KKT attaining pairs, and direct PAVA tests. It prints `ALL_WEIGHTED_ISOTONIC_VARIATION_CHECKS_PASS` when successful.

Finite tests cannot verify an all-dimensional theorem in isolation. The all-dimensional conclusion uses the proved step-column identity, full active-block attainability, piecewise-linear segment decomposition, and the two-point convex-hull formula. General graphs and other loss functions are not covered. Independent audit has not been performed.
