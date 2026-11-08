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

# Reproduction and scientific limits

Execute `python verify_gaussian_cv.py` in a Python 3 environment with SymPy. The accompanying `verification_output.txt` is the captured output of a successful execution: 509 exact-rational/symbolic assertions, including independent direct OLS intercept recomputations, a quadratic-regression slope singularity and a one-dimensional spherical moment simplification.

The mathematical proof of the all-sample-size, all-\(q>0\) cutoff relies on conditional Gaussian projection and the exact integrability criterion for \(\chi_r^{-q}\), not on finite enumeration, simulations, or the output log. Its critical nonzero-numerator witness is written in `RESULT.md`. The program does not establish publication priority, independence of review or correctness of claims for arbitrary integrands beyond the declared quadratic scope.
