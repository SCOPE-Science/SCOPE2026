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

Run `python verify_exact.py` (standard library) to rebuild the rational precision inverse and enumerate the sixty-four partition labels, checking all claimed fractions. Run `python verify_symbolic.py` (SymPy) to independently reconstruct the variable-screening Green inverse, derive and test all six bridge-component gaps plus the specified improving coordinated recoloring, and validate the unique-positive-root bracket. The unrestricted family follows from the analytic weak-leaf construction in `RESULT.md`; no finite checker pretends to exhaust it.

All numbers quoted as exact fractions are calculated from the displayed precision matrix, not fitted numerically. No independent audit or independent external validation is claimed.
