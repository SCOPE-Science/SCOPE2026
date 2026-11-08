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
Run `python verify.py` using Python 3 and SymPy. The checker verifies the scalar-projective optimization identity, an exact nonnegative deficit polynomial identity, a rational bracket for the unique relevant fourth-degree threshold root, independent symbolic one-dimensional Gaussian moments, six exact multivariate Gaussian-moment test cases, and sharp rank-one equality witnesses. The final success line is `ALL_GAUSSIAN_QUADRATIC_HYPERCONTRACTIVITY_CHECKS_PASSED`.

The infinite family of dimensions and arbitrary coefficient inputs is justified by the analytical matrix/Wick proof in RESULT.md, not by the finite sample cases. The verification was performed using the included exact standalone script. Independent audit is not performed.
