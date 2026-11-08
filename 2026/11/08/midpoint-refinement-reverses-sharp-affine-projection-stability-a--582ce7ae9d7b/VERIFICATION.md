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

# Reproducible checks

Run `python verify_midpoint_star_projection.py` with Python 3 and SymPy installed. It constructs each exact rational Gram matrix and performs Gauss–Jordan inversion without importing any precomputed inverse rows. It independently sums the signed absolute integrals for every node for integer degrees \(2\) through \(17\). It symbolically checks all asserted algebraic difference identities, the limit formulas, the derivative, and the positive-coefficient expression controlling the all-degree refinement transition. The actual successful run printed:

```
EXACT_DENSE_GRAM_INVERSION_AND_SIGNED_KERNELS_OK 16
EXACT_UNIVERSAL_COMPARISON_POLYNOMIALS_OK
EXACT_REFINEMENT_REVERSAL_AND_LIMITS_OK
ALL_MIDPOINT_STAR_PROJECTION_CHECKS_OK
```

The analytical proof in RESULT.md establishes the results for all integers \(d\ge2\). The finite arithmetic loop is a reproducibility check, not a proof that the formulas hold for infinitely many degrees. All comparison identities are rederived in exact symbolic arithmetic; no external certificate or independent scientific audit has been performed.
