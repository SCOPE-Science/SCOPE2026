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

The analytical proof in `RESULT.md` establishes the complete theorem. To replay the finite exact independent test, from the package directory run `python verification/check.py`; it uses only the Python standard library and requires no downloads.

The test enumerates all vertex-retention configurations for selected small complete bipartite graphs and compares direct exact rational averages and covariances against the claimed formula. It also checks endpoint signs and dense rational-grid strict monotonicity for additional class sizes. The script completed 713 assertions (including equality-pair counts); finite testing alone cannot verify the infinite family, uniqueness at every parameter, or asymptotic limits.

No independent mathematical audit has been performed. The cited general percolation literature provides context, not a formal novelty certificate.
