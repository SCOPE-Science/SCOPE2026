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

# Verification details

An executable `check.py` is included. It is a reproducible Python 3 script requiring NumPy and SymPy. It uses exact gamma/beta identities and symbolic simplification for the covariance and normalized determinant, differentiates the closed formula, and independently compares tensor-product Gaussian quadrature against the moments and volume for four radius pairs. It also verifies twelve affine-angle determinant transformations. An actual execution completed successfully for all checks from the included source before packaging. The proof relies on exact Fubini identities and algebra, not finite samples. This is self-review only, without independent audit.
