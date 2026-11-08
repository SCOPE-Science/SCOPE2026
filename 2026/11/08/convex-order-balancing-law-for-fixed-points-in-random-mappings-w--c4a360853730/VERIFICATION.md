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

The deterministic checker `check.py` was run with Python 3 using exact rational arithmetic and no external dependencies. Its actual output was:

```
PASS: 636 exhaustive degree vectors of orders 2..6; 3158 exact transfer comparisons
```

For each degree vector it constructs the prescribed-multiplicity word law by full recursion, independently computes the inclusion-exclusion probability generating function, checks every mass, total mean and variance, and then checks all valid transfers against the exact second-difference probability law and all integer stop-loss thresholds. The proof in `RESULT.md` is valid for arbitrary finite \(n\ge2\); the checker is finite confirmation, not a computer proof of the unbounded theorem. Search and comparison limitations are reported separately in `REVIEW.md`.
