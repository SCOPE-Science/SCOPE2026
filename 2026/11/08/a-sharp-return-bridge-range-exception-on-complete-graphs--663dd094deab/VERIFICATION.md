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

Exact integer/rational enumeration in standalone `CHECKER.py` independently counts all fixed-length loopless complete-graph paths, distinguishing their distinct-vertex count and return to origin. The test runs on all integer \(3\le n\le16\) and \(2\le t\le26\), verifies both expectation formulas, the complete strict sign classification, and the finite cases of odd-time stochastic-support incomparability. It reports `PASS: 1246 exact integer/rational assertions` when run using Python 3.

The all-parameter proof is analytic: diagonalize the two finite transition matrices, sum expected indicators, and prove the strict sign of the exact numerator. No finite enumeration was used as an exhaustive verification of all parameters. No external independent audit was performed.
