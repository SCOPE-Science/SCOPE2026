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

# Verification

The package includes `checker.py`, a standalone Python 3 script requiring only the standard library. The command is `python checker.py` after extracting the file. At review, it completed with the lines `PASS 183 deterministic checks` and `PASS 25 local normal-form diagnostics`.

The direct numerical checks cover the exact moving-frame curvature density, critical cross-product zeroes, orthogonality and lengths of the two first-order cross-product derivatives, the algebraic logarithmic coefficient, high-winding convergence, elliptic symmetry, and the limiting cusp profile. The global estimates, smoothness claim, and inverse uniqueness are established in the analytic proof, not by a finite number of tests. No independent audit has been performed; no external certificate is asserted.
