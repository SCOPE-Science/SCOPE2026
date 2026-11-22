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

# Verification and reproducibility

Run `python3 verify.py`. The checker uses only the Python standard library and requires no input data or network access. Its finite statements are exhaustive, not sampled: all identification patterns for three targets and up to four distinct predecessor slots are generated, with all possible equivalences under relabelling of external witnesses. Each directed-constraint probability is the exact rational fraction of linear extensions in a uniform one-coordinate ordering. The two maxima tables and the uniqueness of the leading common-predecessor pattern are checked as exact fractions.

Recorded output:

```
Finite poset certificate: 124 four-edge types, 4 exact assertions
Independent direct sample checks: 11 exact assertions
PASS: 15 exact assertions; all required type maxima reconstructed
```

The program additionally directly enumerates small coordinate-ranking samples for their non-Pareto third factorial moments. These finite checks establish the combinatorial certificates; the asymptotic vanishing of every other diagram follows from the strictly negative exponents shown in the proof. No independent scientific validation has been performed.
