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

The theorem was checked analytically using two independent Gaussian coordinates for the first partial-LU pivot, and two independent chi-squared norms for the CPQR alternative. The normalization by the best rank-one singular-value error was checked explicitly for both choices of row and column.

Run `python3 verify.py` from the same directory as the extracted artifacts. It checks the exact diagonal cross approximation, polynomial beta CDFs for even sketch heights, and the limiting constants. The finite diagnostics supplement and do not replace the analytic result. No independent external audit, general algorithm verification, or finite-precision guarantee has been performed.
