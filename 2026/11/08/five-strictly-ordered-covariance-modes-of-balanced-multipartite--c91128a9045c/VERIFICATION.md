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

# Verification of the covariance spectral classification

The accompanying `artifacts/verify.py` uses exact rational arithmetic for the transfer-current covariance of balanced complete multipartite graphs. It checks the claimed eigenvalue formulas and their dimensions for all 1,606 pairs of integers with 3 <= k <= 24 and 2 <= n <= 74, and diagonalizes five explicit small covariance matrices independently using NumPy. For K_(2,2,2), it enumerates all 384 spanning-tree vertices and checks all 144 covariance entries by exact arithmetic against the transfer-current construction.

Run `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py` with Python 3 and NumPy. A successful check prints `BALANCED_MULTIPARTITE_COVARIANCE_CHECKS_PASSED 1755`. The 1,606 parameter tests, finite exhaustive enumeration and floating point eigenspectra are corroboration, not a substitute for the general proof in `RESULT.md`. The transfer-current identity is a classical external theorem. The complete 2023 Li–Chen–Yan paper was not available for historical comparison; its abstract does not rule out a related calculation. Independent audit has not been performed.
