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

# Reproducibility and verification

Run `python CHECK.py` using Python 3 with SymPy, NumPy and SciPy. The script calculates the exact third-order Taylor terms, verifies the transition coefficient, checks the full two-dimensional projection at multiple directions, and simulates only the two explicitly stated finite resource laws. It reports `ALL CHECKS PASSED` when the internal assertions succeed.

The symbolic calculation is exact. The finite-difference and integration tests are corroborative only, with no logical role in proving the infinite-time result. The proof uses analytic regularity for finite resource support, the symmetry-reduced cubic field and the standard finite-dimensional center-manifold stability theorem. Critical dynamics at \(\kappa=13/12\), global basin geometry, and stochastic learning are not verified.
