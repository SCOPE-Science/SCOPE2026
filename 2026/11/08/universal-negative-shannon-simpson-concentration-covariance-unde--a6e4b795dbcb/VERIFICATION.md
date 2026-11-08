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

`check_covariance.py` runs exact differentiated-beta-moment arithmetic against the two independent algebraic presentations, and high-precision direct numerical integration for two-category Dirichlet laws. The tested 1,360 positive-integer parameter vectors have lengths \(m\in\{2,3,4,5\}\) and coordinates in \(\{1,2,3,4\}\). On each it checks both formula equivalences and strict negativity; symmetric vectors additionally test the closed specialization. Four real-valued beta laws are integrated independently with an endpoint-smoothing substitution; absolute deviations from the closed formula were below \(10^{-45}\) in the checked environment. All checks passed.

Run `python check_covariance.py` with Python and `mpmath` available. The program's exact rational checks use Python standard-library `fractions.Fraction` and `itertools.product`.

The computation does not prove the infinitely many parameter cases. The accompanying analytic proof uses gamma-function differentiation, a weighted pairwise covariance identity, and strict monotonicity of the digamma function. No independent audit or independent validation has been performed.
