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

Run `python verify_crisis.py` with Python, SymPy and mpmath. A successful run prints `LOZI_CRISIS_TANGENCY_CHECK_OK symbolic_first_levels=8 numerical_root_cases=18`.

The checker directly differentiates the first exact radical crisis equation at its degenerate root, verifies the solved first-derivative recurrence at eight depths symbolically, and solves the original, untruncated equations at six levels for three small positive determinants apiece with 75 decimal digits. The infinite family of statements is proved by the recurrence solution and analytic implicit-function theorem in RESULT.md. The numerical samples test consistency; they do not certify an infinite statement or prove the analytic local branch's global uniqueness.

The published formulas for the renormalisation map, homoclinic-corner function and attractor-component regions are cited explicitly in RESULT.md. Their dynamical interpretation is relied on as established literature; the new statement proves the additional perturbation coefficients and local side identification.

Independent audit: not performed.
