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

# Reproducible checks and limits

Run `python check_double_star.py` with standard Python 3; there are no external dependencies. The script directly computes the uniform-vertex variance on every signed edge-increment configuration for 64 parameter pairs with \(1\le a,b\le8\), verifies all equality profiles, and uses separate integer arithmetic to maximize over all two-class count pairs for 6,400 examples. It verifies the strict fixed-vertex balancing order for up to 300 leaves and checks the sharp change of optimizer type for small-side counts through 99. The final success marker is `ALL_DOUBLE_STAR_LIPSCHITZ_SPREAD_CHECKS_OK`.

The genuine infinite proof is in RESULT.md. Finite enumeration alone would not establish strict convexity for all tree sizes, optimizer completeness, the crossover, or the fixed-order balance law; those are proved by the edge-cut quadratic coefficient, diagonal saturation and explicit integer-square optimization. Proof and checker use uniform vertex measure only, not arclength. The absence of an independent scientific audit is not a mathematical validation claim.
