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
# Verification record

Run from the package directory with `python verify.py` (Python 3 standard library, no optional dependencies).

The actual program output was:

`THETA_VERIFY_OK exact_rational_cases=10 jump_groups=24 recovered=10 independent_pair_samples=320000 cdf_comparisons=20 max_abs_cdf_error=0.0026625`

The verifier uses exact rational arithmetic to clip the distance-tail polygons and integrate same-path tails for ten different positive rational path triples, encompassing strictly ordered lengths and each tied-length pattern. It checks all 24 distinct jump-radius groups in those examples and confirms that the reconstructed parameter multiset agrees with the input in all ten cases. In a separate randomized computation, 320,000 independent arclength-uniform pairs were used for 20 empirical-versus-exact cumulative distribution comparisons; the maximum observed absolute discrepancy was 0.0026625. This is a reproducibility check, not an infinite-parameter certificate; the proof is the polygon-area argument in `RESULT.md`. All literature comparisons and scientific priority conclusions remain subject to independent assessment.
