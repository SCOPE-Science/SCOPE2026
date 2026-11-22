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

# Reproducible verification

Run `python3 verify.py` with Python 3's standard library. The script uses 70-digit decimal arithmetic and bisection to locate the unique zero of a strictly decreasing log-determinant derivative. It checks the scalar contact equalities for all 361 pairs of integer parameters \(2\le a,b\le20\), and the exact-form polynomial relationships, including both degenerate explicit cases \(b=2,3\). It then independently constructs the complete vertex list, probability design, mean, full covariance matrix and every contact gauge in all 49 configurations \(2\le a,b\le8\).

Expected successful output:

```
CLIPPED_RANK2_LOEWNER_PASS scalar=361 full_covariance_and_contacts=49
```

The tolerance is \(10^{-45}\), with 70 digits of working precision. Tests are finite high-precision corroboration rather than a proof for unrestricted integers. The mathematical proof uses symmetry, covariance splitting, strict log-determinant concavity, and the trace/determinant inequality for competing ellipsoids. No external independent audit has been performed.
