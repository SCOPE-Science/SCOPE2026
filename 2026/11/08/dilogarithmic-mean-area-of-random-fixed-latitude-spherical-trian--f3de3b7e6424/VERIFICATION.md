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

Run `python checker.py` with Python 3; no third-party Python packages are needed. It samples 85,000 independent triples at each of four fixed colatitudes and computes area by both the independent solid-angle determinant formula and the three-vertex Girard angle sum, requiring their pointwise agreement. It then compares the resulting sample mean with the analytic dilogarithm expression using a variance-aware error bound. It also verifies the \(r=1\) dilogarithm endpoint to numerical tolerance.

The exact proof, not this stochastic simulation, certifies the identity for every permitted colatitude. The unreviewed historical cap-shape article remains a literature-priority risk. No external mathematical audit has been performed.
