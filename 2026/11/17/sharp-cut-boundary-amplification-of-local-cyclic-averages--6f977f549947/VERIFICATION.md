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

This package includes `verify.py` (Python standard library only). Execute `python verify.py` after extracting the complete finding. The script reconstructs the cyclic moving-average action directly and computes path variation using exact rational numbers; it does not import proof formulas into the operator under test except to compare their predicted values.

Actual complete run:

```text
EXACT_UNIFORM_ALL_N2_TO_N30_ALL_WINDOWS_PASS 464
EXACT_LOCAL_SUPPORT_MASS_LAW_PASS 6488
EXACT_BINOMIAL_INITIAL_TRANSIENT_PASS 380
EXACT_DIRECT_TERNARY_INPUTS_PASS 21321
LONG_TIME_EXACT_FINITE_SANITY_PASS
ALL_CYCLIC_OPEN_PATH_VARIATION_CHECKS_PASS
```

The direct ternary-input test is finite, and the long-time diagnostic uses a finite iteration count. Neither proves the infinite-dimensional or all-parameter theorem. The proof in `RESULT.md` covers arbitrary finite dimensions and real probability weights under the stated support hypotheses; Fourier decay establishes the true fixed-dimensional limit. No independent audit or external formal verification is claimed.
