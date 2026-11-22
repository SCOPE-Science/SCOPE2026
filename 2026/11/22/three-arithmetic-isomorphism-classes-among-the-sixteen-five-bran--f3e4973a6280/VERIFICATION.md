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

Run `python3 verifier.py` from the extracted package directory. The standalone program enumerates all 16 twists, the 20 affine group elements, and the 16 exact branch-character signatures; it independently counts every \(\mathbb F_5\)- and \(\mathbb F_{25}\)-point through explicit local-fibre formulas and counts all five elliptic double covers.

Observed output:

```
HUMBERT_F5_FIVE_BRANCH_TWISTS_VERIFIED
16 twists; affine group 20; orbit sizes 1,5,10; F5 point counts 16,8,0; all F25 point counts 56
```

The computation has finite, fully exhausted domains. Kummer squareclass independence, genus, elliptic cohomology decomposition, the effect of base change on quadratic extensions, and equivalence of all twists within each orbit are justified separately in RESULT.md. An infinite family of finite fields or every possible arithmetic form is not claimed. Independent audit has not been performed.
