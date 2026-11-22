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

# Reproducibility

Execute `python3 checker.py`. The program has no mandatory external dependencies. It enumerates every spin configuration for sizes 3 through 9 and five signed rational biases; tests positivity of each jump rate, reverse-rate symmetry, exact generator action on the distance-two observable, exact drift and corrected martingale bracket, and the closed variance coefficient. The size-three checks are solely a consistency check. It ran successfully with 132,990 exact-rational assertions. With NumPy present, the optional 4-, 5- and 6-site tilted-generator eigenvalue curvature checks also passed (three comparisons).

The all-size result relies on the explicit generator and martingale calculation in RESULT.md. No finite enumeration is used as proof for all sizes. The long-time limit is taken before any large-size limit. Prior relevant literature and unresolved publication-priority risks are identified in REVIEW.md.
