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

# Verification details

The standalone `verify.py` was run with Python 3 using only standard-library modules. It generated each nonplane rooted labeled binary topology once via every-edge insertion and independently computed the cherry, balanced-four-leaf and asymmetric-four-leaf fringe counts. For \(n=4,5,6,7,8\), the enumerated rooted tree totals were respectively \(15,105,945,10395,135135\), matching \((2n-3)!!\). Exact first moments, both mixed covariances, the sign assertions and simplified formula identities passed in a total of **146650 exact integer/rational assertions**.

This is finite verification, not an exhaustive check of all sizes. The universal theorem follows from the explicit contraction/laminarity proof in `RESULT.md`. No external independent validation has been undertaken. Full-text comparisons were available for the cited 2009, 2015 and 2024 technical works, and the 2018 induced-quartet article had an accessible text version; historical implicit coverage remains possible.
