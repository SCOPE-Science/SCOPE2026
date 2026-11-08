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

# Reproducibility and limits

Execute `python3 verify.py` alongside `RESULT.md`. It produces 4,425 exact rational assertions and enumerates every recursive-tree attachment and edge-state pattern for all sizes up through seven vertices, for three rational retention probabilities. It independently checks the exact finite mixed-moment, covariance and root-cluster variance identities against brute-force probabilities, and cross-checks analytic moment recurrences for a wider range of sizes and parameters.

The infinite sign claim is proved by the product bounds in `RESULT.md`. The fixed-parameter asymptotic, positive variance constants, inverse-square-root correlation law and high-retention limits require the written gamma-ratio and recurrence arguments, not a finite numerical extrapolation. Random sampling is not used. Full historical priority is not independently certified; the nearest inspected literature provides separate marginals and other cluster statistics.
