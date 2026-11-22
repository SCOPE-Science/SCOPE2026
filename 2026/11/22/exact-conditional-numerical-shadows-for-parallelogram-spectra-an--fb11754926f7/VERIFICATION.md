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

# Reproducibility

With Python 3, run `python verify.py`. The expected exact-arithmetic result is `PARALLELOGRAM_NUMERICAL_SHADOW_EXACT_CHECK_OK 3853`.

The script tests the inversion of four Walsh coordinates, feasible conditional intervals and their midpoint identity, normalization and Beta-integral coefficients, and the ratio of nonlinear to affine squared loss, using rational arithmetic only. Its finite grids do not prove probability laws over all continuous parameter values. Those follow from uniform Dirichlet coordinates, the constant Jacobian, exact interval geometry, and orthogonal conditional-expectation projection given in RESULT.md.

The record is subject only to self-review; independent audit has not been performed.
