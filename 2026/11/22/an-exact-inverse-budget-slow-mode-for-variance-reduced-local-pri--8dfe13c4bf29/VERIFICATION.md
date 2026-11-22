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

The proof verifies conditional gradient-estimator unbiasedness, closes the first-moment recursion on affine quadratic gradients, establishes its fixed point and zero-sum dual subspace, and obtains the positive weighted-graph eigenvalues by a semisimple perturbation expansion. The exact two-agent stochastic example and its work count follow from a scalar recurrence. All quantifiers and excluded mean-square claims are stated in `RESULT.md`.

Execute `python check.py` with Python 3 and NumPy available. The included checker completed 3,840 exact-rational two-agent trajectory assertions, 144 exact-rational enumerations of every within-round SAGA sample path, and 960 supplementary numerical spectral assertions on deterministic positive-definite mixing matrices.

Finite numerical checks are diagnostic, not proof for all sizes or arbitrarily large local budgets. All claims are restricted to exact scalar component quadratics, symmetric positive-definite mixing, independent uniform component selection, and first moments. A separate independent mathematical audit has not been performed.
