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

The result is proved analytically in `RESULT.md`; the six-step proof includes a trace-class Bochner representation, uniform geometric-law variance bound, dyadic Hilbert–Schmidt estimate, disjoint-block trace-norm obstruction, Schatten interpolation, and infinite-rank rational-function argument. Each step identifies all parameter ranges and its endpoint scope.

Execute the standard-library diagnostic checker using `python3 check.py`. On the current package it reports `PASS: 6889 finite skewness, block, trace-lower-bound and HS-upper-bound checks`. An independent direct finite-section singular-value experiment on dimensions 32, 128, 256 showed shrinking Hilbert–Schmidt norms with positive nuclear norms; such experiments do not establish infinite-dimensional estimates or optimal constants. The checker cannot prove infinite-rank conclusions or uniqueness of prior results.

The trace-norm lower limit is bounded below by \(\log(7/5)/(8\log2)\), whereas the exact limit and any optimal value remain unknown. The asserted \(\mathcal S_p\) rates are upper bounds. No independent audit has been performed.
