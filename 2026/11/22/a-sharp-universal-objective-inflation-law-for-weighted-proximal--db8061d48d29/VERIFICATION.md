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

The proof establishes the bound for every finite-dimensional real convex nonnegative one-homogeneous regularizer with positive ridge curvature. The supporting script `verify.py` uses the Python standard library and exactly checks rational weighted-box examples, the dual-projection formula, the nonnegative slack identity, and sharp instances. Execute `python3 verify.py` from the directory containing this file and the script. Finite checks cannot prove the universal statement; the metric-projection and duality argument in RESULT.md supplies that proof. Historical priority is not independently verified.
