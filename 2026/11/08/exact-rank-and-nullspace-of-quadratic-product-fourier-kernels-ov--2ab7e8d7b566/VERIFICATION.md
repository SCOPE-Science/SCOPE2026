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

# Reproducibility checks
Run `python3 CHECKER.py` with NumPy installed. The finite verification output is `QUADRATIC_PRODUCT_RANK_CHECK_PASS`, followed by the actual integer and complex-SVD case counts. The exact root-census checks are modular arithmetic; the matrix ranks are corroborating floating-point computations with stated zero/nonzero thresholds. The proof's universal claims depend on the character decomposition and cyclotomic argument in `RESULT.md`, not on finite enumeration. No independent validation has been performed.
