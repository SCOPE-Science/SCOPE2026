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

The exact finite certificate `free3_certificate.json` contains thirty canonical multiplicative word representatives and \(778\) masks encoding explicit finite nonempty sums. The checker `verify.py` evaluates every witness on the entire \(125\)-element input cube, asserts all witnesses distinct, checks generator inclusion, verifies closure under both operations, and independently performs additive closure to confirm completeness.

It also exhaustively constructs the free-algebra spectra in ranks one and two and checks the word-function count in all three ranks. Successful local execution produced:

```
VERIFY_OK: free ranks 1,2,3 = 2,21,778; full-support counts 2,17,721; word ranks 2,8,30; 778-element explicit certificate closed under both operations
```

No sampling is used for those three finite ranks. The proofs for arbitrary finite rank rely on the pointwise multiplication table, the injective first-occurrence word classification, and content invariance, not on a computer extrapolation.

The verification does not establish any value for \(|F_r|\) when \(r\ge4\), historical uniqueness, or an independently audited proof. The source and exact mathematics are in `RESULT.md`.
