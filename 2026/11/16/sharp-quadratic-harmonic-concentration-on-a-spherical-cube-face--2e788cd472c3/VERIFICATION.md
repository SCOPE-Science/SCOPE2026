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

# Reproducible checks

The included `verify_cube_face.py` uses exact symbolic linear equations for four regional fourth-order moments, checks that their solutions equal the stated formulas, and proves algebraically that the resulting five normalized eigenvalues equal the stated values and have the required trace. It tests strict ordering and positivity separately.

An independently implemented tensor Gauss–Legendre quadrature evaluates each of the 25 local Gram matrix entries directly from the gnomonic parametrization, without using the solved moment formulas. With orders 24, 40, 64 and 100 the maximum absolute discrepancy from the predicted diagonal matrix was respectively \(5\cdot10^{-16}\), \(2.11\cdot10^{-15}\), \(1.22\cdot10^{-15}\) and \(2.16\cdot10^{-15}\). The proof's universal quantifiers are established by exact identities and the finite-dimensional spectral theorem, not by finite sampling.

Run with `python verify_cube_face.py`; dependencies: `sympy`, `numpy`, Python 3. A separate independent mathematical review has not been performed.
