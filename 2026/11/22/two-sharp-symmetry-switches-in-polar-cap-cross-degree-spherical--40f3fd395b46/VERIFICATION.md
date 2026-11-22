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

# Reproducibility and boundaries

From this directory run `python verify.py` with SciPy and SymPy installed. The included `verification_output.txt` records the completed execution of that script. The checker uses independent adaptive integration over the cap-height variable, compares with normalized analytic formulas in nine dimensions, verifies exact polynomial and transition-defect identities using SymPy, and checks the two-stage top-sector ordering at selected cap heights. It reports 308 passed assertions.

The mathematical proof is contained in `RESULT.md`: the checker is a reproducibility aid, not an infinite-dimensional, all-parameter certificate. No independent mathematical audit or external validation has been performed. The source-kernel nullspace is structural, and the quoted condition number refers only to positive singular values.
