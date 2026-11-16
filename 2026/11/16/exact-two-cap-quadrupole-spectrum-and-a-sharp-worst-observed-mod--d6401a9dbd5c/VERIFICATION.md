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

# Checks and their limits

`python verify.py` symbolically reconstructs the complete five-by-five regional Gram matrix from first-principles spherical monomial moments, checks the full-sphere norm matrix, confirms all four eigenvalue branches and six exact difference identities, and verifies the trace. It also independently computes cap quadratures at seven aperture values (including both crossing apertures) and compares all five numerical eigenvalues to the analytic formulas. The checker was executed successfully, printing:

```
ORTHOGONAL_DUAL_CAP_QUADRUPOLE_PASS exact_gram=25 branch_differences=6 quadrature_radii=7 transitions=5/9,11/15
```

The proof does not infer infinite-aperture validity from seven samples. The exact integration and factorizations establish the theorem for the entire specified continuous aperture interval. No independently conducted audit is claimed. Geometric and bibliographic scope restrictions are documented in RESULT.md.
