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

Run `python checker.py` with Python 3.9 or later. It requires no third-party packages and reports 3128 exact-rational assertions passed, covering 17 sample sizes and 18 interior rational thresholds per size. Its checks include the exact upper-envelope value in the three regimes, the disjoint-band geometry and complement measure, the success/failure density identities required for marginal uniformity, and incompatible positive larger-threshold targets. The proof of optimality and rigidity for all admissible real parameters is written in RESULT.md; it does not depend on the checker. Independent audit has not been performed.
