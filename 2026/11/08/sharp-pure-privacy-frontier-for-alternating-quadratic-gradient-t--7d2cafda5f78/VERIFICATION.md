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

Run `python3 verify.py` with Python 3's standard library. The checker uses exact rational arithmetic and independent conditional executions rather than relying on floating-point iteration. It verifies the sensitivity cone and finite generating-function identities over a parameter grid; explicitly constructs heterogeneous-curvature objective instances sharing all communicated messages; and checks finite-prefix Laplace likelihood-ratio attainment.

It also verifies the exact rational certificate for \(h=1\), \(\alpha=1/2\), \(r=4/5\) and unit scales and adjacency radius: the sharp privacy parameter is \(84/19\).

These tests are finite. The proof of the infinite-transcript necessary-and-sufficient condition is the analytic eigenvalue and exact-likelihood argument in `RESULT.md`. No independent or external mathematical audit has been performed, and no verification claim is made about altered algorithms or vector objectives.
