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

## Reproduction
Run `python check.py` with Python, SymPy, mpmath, NumPy and SciPy installed. It constructs every listed integer Kalman matrix from the original path Laplacian, checks the coprimality/absolute-determinant rule exactly, tests the explicit modal Gramian determinant at high precision, and computes independent physical-coordinate finite-time Gramian quadratures.

The checker reports 602 successful finite assertions on the tested parameter grid. Generality for every path order and every positive finite horizon follows from the proof in `RESULT.md`, not from finite enumeration or a numerical tolerance.

## Limits
The independent quadrature uses floating-point arithmetic and is only a corroborative check. The primary proof is a symbolic spectral and integer argument. No independent human audit has been performed; publication priority is subject to further literature scrutiny.
