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

# Reproducibility and verification scope

Run `python3 verify.py` from the extracted package. It requires Python 3 and only standard-library modules (`fractions`, `math`, `random`). The script checks coefficients of rational polynomial expansions for two-step stage maps, exact uniform moments, and the sine benchmark by numerical quadrature and a seeded Monte Carlo diagnostic.

These finite checks corroborate the local algebra and normalization, but are not an exhaustive proof over arbitrary stage couplings, arbitrary smooth vector fields, or asymptotic limits. The proof in `RESULT.md` establishes the global pathwise bound, Lindeberg condition, covariance normalization, and uniqueness on a scalar linear test. Any reimplementation should use \(h=T/(2n)\) and exact antithetic pairing \(V=1-U\) within each pair. Scientific precedence requires independent specialist verification.
