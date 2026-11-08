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

# Reproducibility and proof boundary

The exact rational checker `CHECK.py` differentiates the original four-coordinate update at a two-agent admissible fixed point, validates the stationary residual, confirms all rational Jacobian entries and its symbolic characteristic polynomial, then verifies the closed-form weighted-moment spectrum. Additional separate rational reduced-matrix cases confirm rank, trace and product with three and four agents. Execute `python CHECK.py` using Python 3 and SymPy.

The proof for arbitrary finite population size is the rank-two factorization and strictly negative determinant in `RESULT.md`, not any sampled enumeration. No proof has been given for stochastic learning, a different self-play derivative convention, boundary projection effects, global attraction or nonlinear behavior along unit-multiplier directions. Literature originality may depend on results not indexed by the surveyed resources. Independent validation has not been performed.
