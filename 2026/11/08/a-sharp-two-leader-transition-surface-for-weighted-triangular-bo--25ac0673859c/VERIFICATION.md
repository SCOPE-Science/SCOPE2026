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
# Reproducibility

Run `python3 verify.py` in a folder containing this file and the provided `verify.py`. The program constructs the weighted graph Laplacian directly and tests all two-element leader sets using exact `fractions.Fraction` Gauss–Jordan inverses. It checks 157 combinations of integer page count and rational edge weights, including threshold ties, 5,814 exact matrix computations, all four closed forms, and the complete optimal-set classifications.

Expected output:

```
VERIFY_OK configurations= 157  exact_pair_matrices= 5814  class_formula_checks= 5814  optimizer_checks= 157  leaf_exclusion_checks= 157
```

The proof in RESULT.md is the evidence for all real positive weights and all integer sizes. The finite checker is a reproducibility diagnostic, not an infinite certificate. No independent audit has been performed.
