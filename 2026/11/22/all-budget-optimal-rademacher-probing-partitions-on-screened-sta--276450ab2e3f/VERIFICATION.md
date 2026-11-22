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

Run `python verify.py` in Python 3 with the standard library only. `VERIFY_OUTPUT.txt` contains the independently replayed stdout and completion status. The checker exactly inverts the shifted star Laplacian over rational numbers for seven shifts, with \(m=2,\ldots,7\), enumerates all set partitions into every budget \(3\le k\le m+1\), and compares each directly evaluated squared-resolvent weight to the analytic formula. It also verifies global minima, the strictly increasing discrete first differences, and selected exact ties. It completed 35,280 exact partition tests.

This computation checks finitely many integer sizes and rational shifts; it does not prove the theorem for all integer budgets, all star sizes, or all positive real shifts. The universal proof is the explicit resolvent inversion and integer balancing/discrete-convex argument in RESULT.md. No independent audit has been performed.
