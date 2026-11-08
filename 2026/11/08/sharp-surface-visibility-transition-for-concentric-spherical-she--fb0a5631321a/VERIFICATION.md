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

# Reproducible scientific checks

Run `python verify_surface_shell_visibility.py` from this package. The script uses only the Python 3 standard library and a fixed random seed. A successful execution prints the `VERIFY_OK` summary of 28 combined rational and monotonicity/special-case checks, eight independent direct-segment simulations, and exercised thin-shell, critical-Gaussian and off-critical large-deviation regimes.

The exact arithmetic integrates the odd-dimensional angular density polynomial with `fractions.Fraction`, independently of the geometric segment classifier. The simulations generate two area-weighted boundary components, draw independent normalized Gaussian directions, and explicitly minimize the squared Euclidean radius along the connecting segment. A small absolute floating-point tolerance prevents misclassification of exactly tangent inner-boundary endpoints. Numerical quadrature uses composite Simpson integration in the **angle** variable, for which the integrand is smooth at the endpoints. The checker is a reproducibility diagnostic rather than a computer-assisted proof of general quantifiers.

The analytic proof in `RESULT.md` establishes the exact formula in every integer dimension at least two, strict monotonicity, the Gaussian window, the fixed-ratio rare-event equivalent and the fixed-dimension thin-shell limit. No large-dimension uniformity for ratios approaching the endpoints is inferred. Independent examination of the mathematical result has not been performed.
