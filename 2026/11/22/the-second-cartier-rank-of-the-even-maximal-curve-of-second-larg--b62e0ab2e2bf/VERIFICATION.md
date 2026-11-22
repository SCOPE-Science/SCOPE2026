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

The proof independently computes the pole valuations and different using the explicit uniformizer \(y^2/x\), establishes a complete holomorphic basis, and derives the Cartier operator on that basis by separating-variable extraction. The polynomial injectivity lemma and exhaustive parity-index count establish the formula for all \(q=2^n\ge8\).

Run `python3 check_cartier.py` with the standard Python interpreter. The script requires no external packages. It constructs binary Cartier columns from the differential basis, obtains \(\mathcal C^2\) by exact bitwise matrix multiplication, and determines both ranks by exact Gaussian elimination. Verified outputs:

```
q=8 genus=12 rank_C=8 rank_C2=4 formula=4 verified
q=16 genus=56 rank_C=40 rank_C2=26 formula=26 verified
q=32 genus=240 rank_C=176 rank_C2=124 formula=124 verified
q=64 genus=992 rank_C=736 rank_C2=536 formula=536 verified
```

The checks establish finite instances and guard against indexing errors, not an infinite-family theorem by enumeration. The general theorem is proved mathematically in RESULT.md. Comparison with the 2021 \(a\)-number calculation and the 2026 Galois-line paper was made directly against their mathematical statements; unindexed equivalent computations remain possible. No independent mathematical audit has been performed.
