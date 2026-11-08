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

The supplementary `verification.py` is executable with the Python standard library. On this package it reports 3023 successful exact/finite assertions and two seeded simulation diagnostics (3025 assertions total). It checks all early Bernoulli attachment strings through nine vertices, the exact tooth and ray lengths of completed runs, and the finite first-step systems for simple-walk hitting means. It checks the claimed rational reward-variance formula for 77 rational values of \(q\) and compares a seeded Monte Carlo fluctuation variance against \(4pq/3\).

The infinite-tree decomposition, random-time-change argument, functional central limit theorem and almost-sure normalization are mathematical deductions given in RESULT.md, not conclusions from numerical tests. No independent external validation has been performed.
