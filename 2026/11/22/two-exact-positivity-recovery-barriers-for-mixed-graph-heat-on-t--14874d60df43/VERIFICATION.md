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

## Analytical verification

The four-mode orthogonal diagonalization of the explicit path Laplacian yields exact transition formulas. The sign-variation bounds on exponential polynomials prove precisely one positive zero of each of the two potentially negative entries, including multiplicity accounting at the origin. The small-strength rates are determined by joint Taylor expansions; large-strength rates arise from the pure-squared-Laplacian limit.

## Computation

`python check_p4.py` independently compares 400 SciPy matrix exponentials to the derived analytic entries, checks adjacent-entry signs, finds both positive roots for eight strengths, and checks the small-strength ratios. Output ends with `EXACT_SPECTRAL_FORMULAS_NUMERICALLY_REPLAYED 400`, `TWO_DISTINCT_SIGN_CROSSING_TESTS_PASS`, and `ASYMPTOTIC_SMALL_PARAMETER_SANITY_PASS`. Numerical tolerance is about 2e-11 on spectral comparisons.

## Unproved extensions

No global ordering between the two roots at arbitrary mixing strength, no unique optimizer, and no extension to weighted graphs or other vertex counts has been proved. Independent mathematical audit has not been performed.
