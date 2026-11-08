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

# Reproducibility checks and limits

Run `python3 check.py`. It uses no third-party modules and prints `NILPOTENT_WALK_EXACT_CHECKS_PASS` after all assertions. The script independently constructs nonzero rank-one nilpotent generators, counts rational eigenlines, computes additive character sums, and compares the resulting spectral chi-square identities to direct integer convolution for three steps. Checks cover \((q,n)=(2,2),(2,3),(3,2),(4,2),(5,2)\), using genuine extension-field arithmetic for \(q=4\).

The checker does not prove the infinite-dimensional limit, Gaussian-binomial class count for arbitrary size, or the total-variation cutoff. Those claims depend on the complete proof in `RESULT.md`, especially the unique large-eigenspace bijection, uniform large-codimension bound, and the rank-support lower bound. Independent audit and external validation have not been performed.
