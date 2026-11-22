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

## Reproducible verification
Run `python check.py` with Python 3 and SymPy. The self-contained checker constructs the tridiagonal screened path, applies the two symmetric negative-edge updates, calculates exact Schur complements, and independently inverts the full matrices at exact rational parameters for each dimension from four through twelve. It also symbolically compares all distinct entries of the four-terminal adjugate with their proposed formulas.

The executed program reported 1,377 passed exact assertions. All tested below-threshold inverses are strictly positive; the opposite-endpoint inverse entry becomes strictly negative at checked parameters above the threshold and below the positive-definiteness limit. No floating-point comparison is used for an asserted inequality; printed decimal thresholds are illustrative only.

## Limits
The infinitely many graph sizes and all real interaction strengths are certified by the analytic continuant, Schur-complement, and adjugate inequalities in `RESULT.md`, not by finite enumeration. The public mathematical review is same-model only; no independent external mathematical audit has been performed.
