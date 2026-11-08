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

The exact proof is in `RESULT.md`, sections 1–5. The principal nonstandard lemma is the sharp two-level reduction: in each ordering chamber, top-minus-bottom support width is linear, every centered normal is a nonnegative sum of step rays, and strictness of the Euclidean triangle inequality excludes all combinations of two distinct rays as minimizers.

To perform the finite replay, run `python verify.py` from a directory containing the embedded `verify.py`. The program uses exact rational arithmetic for all width comparisons and does not require external packages. Its output was:

`HYPERSIMPLEX_WIDTH_CHECKS_PASSED grid_profiles= 566297 weighted_profiles= 4 phase_boundaries= 5`

Finite grid tests are not universal optimization proofs. The exhaustive subset minimization is used only for the small checker profiles. The infinite parameter domain is proved analytically in `RESULT.md`. No external independent audit has been performed.
