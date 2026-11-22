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

# Reproducible checks and boundaries

Execute `python curvature_transfer_check.py`. Exact rational arithmetic checks the two absolute Hermite kernel integrals, one-jump norms for representative convex and extrapolating weights, and 1,000 generated rational inputs and mesh lengths. All run successfully. The proof for arbitrary bi-infinite grids, real weights and arbitrary `ell^1` jump data is analytic; no finite test certifies its infinite quantifiers.

The expected final marker is `ALL_SECOND_ORDER_VARIATION_TRANSFER_CHECKS_PASS`. Historical novelty is qualified by a complete-text access limitation for Aràndiga (2013); no independent audit is asserted.
