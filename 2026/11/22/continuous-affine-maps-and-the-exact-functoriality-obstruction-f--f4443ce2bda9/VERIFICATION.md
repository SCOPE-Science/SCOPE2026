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

The proof is an arbitrary-rank coordinate argument, not an extrapolation from computation. Unique factorization and the signed-divisor topology are explicitly attributed to the cited motivating source. The exact reduction of minimal numerator-denominator divisibility to signed coordinate extension is used in each proof step.

The accompanying `check_affine.py` was run using Python 3 and reported:

```
PASS 729 affine 2x2 integer models; 121 comparable domain pairs each
PASS explicit injective monoid-map discontinuity witness
```

The checker exhaustively verifies a bounded family only. The arbitrary-rank conclusion follows from the proof's two-coordinate obstruction and its finite-support reduction. There is no independent audit or external certification.
