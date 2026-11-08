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

The exact proof is in `RESULT.md`. The standalone Python standard-library checker is `verify.py` and is executed with `python3 verify.py`. It exhaustively enumerates cycle stable sets of lengths \(3\) through \(16\), compares the complete two-point moment kernel as exact rational fractions, and checks the analytic Fourier spectrum and principal-axis classification for these sizes. Further numerical order tests cover \(17\) through \(250\). The finite checker establishes only these stated finite checks; the all-dimensional claims rest on the closed symbolic derivation and inequalities. No independent external mathematical audit has been performed.
