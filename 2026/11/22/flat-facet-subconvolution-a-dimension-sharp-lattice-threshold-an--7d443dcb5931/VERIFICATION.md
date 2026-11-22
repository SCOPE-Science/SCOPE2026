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

The theorem is proved by explicit cubical shell counting and estimates, not by numerical evidence. For \(p>d\), summability of \((1+\|k\|_\infty)^{-p}\) provides a global convolution-ratio bound. For \(p\le d\), the full norm-equality region on coordinate rays yields the power/logarithmic divergence, and its complement has a strictly lower asymptotic order. The checker can be run as `python checker.py` (standard library only) and provides independently enumerated finite cubical equality-region checks and finite-truncation diagnostics. Tail terms beyond the truncation are omitted by the checker; these diagnostics are not certified infinite computations. Formula (3) in the proof controls the entire omitted infinite complement analytically.
