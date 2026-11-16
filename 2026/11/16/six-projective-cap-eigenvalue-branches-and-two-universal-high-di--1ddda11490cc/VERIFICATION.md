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

# Mathematical verification

The standalone Python/SymPy checker `cp2_cap_verify.py` was run from this package's content before inclusion. It checks symbolic Jacobi derivative identities with symbolic dimension, the complete branching multiplicity sum and the invariant-kernel trace identity, strict-minimum difference factorizations, the high-dimensional polynomial envelope differences, and separately evaluates exact rational Beta polynomial integrals for dimensions 3 through 8 at cap thresholds 1/7, 2/5, and 4/5. It returns:

```
CP2_SIX_JACOBI_BRANCHES_EXACT_PASS
CP2_MULTIPLICITIES_AND_STRICT_MINIMUM_PASS
CP2_FIXED_VOLUME_TWO_TRANSITIONS_PASS
CP2_DIRECT_EXACT_BETA_INTEGRALS_PASS dimensions=3..8
```

This checker uses symbolic algebra for the general polynomial identities. Its finite exact integrations are a cross-check, not a substitute for the Jacobi decomposition proof, which is included in RESULT.md. Full independent proof audit and independent source-priority certification have not been performed.
