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

# Exact checks and limits

Run `python3 verify_liouville_stride.py` from a directory containing the standalone checker. It requires Python 3 and no external packages. The observed output was:

```
LIOUVILLE_STRIDE_BALANCE_EXACT_CHECK_OK 128834
```

The checker uses exact `fractions.Fraction` rational arithmetic to test the binary recurrence and three-way zero criterion for window lengths up to 2000 and two-adic stride valuations through seven; it checks unit-stride invariance with odd multipliers one, three and five, and compares exact integer product/LCM Liouville signs against prime-local signs over complete periods for windows up to eight and strides up to twelve. It also checks the mean factorization. These tests support reproducibility but do not replace the all-parameter proof in RESULT.md.

No independent mathematical audit or independent external validation has been performed. A bibliographically unindexed equivalent theorem cannot be ruled out by the recorded searches.
