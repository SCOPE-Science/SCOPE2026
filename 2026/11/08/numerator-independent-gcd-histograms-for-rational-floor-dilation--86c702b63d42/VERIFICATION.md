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
Run `python3 verify.py` using the standard Python library; no external packages or network access are required. The recorded replay of the embedded checker gave:

```
EXACT_BLOCK_HISTOGRAMS_OK cases=276 q=2..11 blocks=0,1,2
UNIMODULAR_GCD_IDENTITY_OK cases=2133 q=2..699
MASS_IDENTITY_OK cases=98 q=2..99
SAMPLE q=5 L=12 block=0 p=2 or 3: d=1 count=33 d=2 count=10 d=3 count=5 d=4 count=4
VERIFY_OK arithmetic=exact finite_checks_do_not_replace_general_proof=true
```

The first test independently enumerates all gcd values for the complete tested blocks; the second checks unimodular identities on randomly but deterministically sampled exact integers; the third verifies the totient mass identity with exact fractions. A finite test cannot prove the all-denominator theorem, the natural-density assertion, or the large-denominator asymptotic: those are established by the symbolic argument in RESULT.md. No independent mathematical audit has been performed.
