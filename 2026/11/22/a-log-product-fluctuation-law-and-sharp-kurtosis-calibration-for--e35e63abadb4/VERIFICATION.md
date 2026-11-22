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

# Verification and reproducibility

Run `python3 checker.py` using Python 3 and no third-party libraries. The program checks exact integer polynomial identities for the monotonicity factor; numerical Gamma-moment formula consistency, Brownian endpoint and fine-grid monotonicity; and seeded direct samples from the stationary exponential-times-Gamma representation for increasing sluggishness. The expected output concludes `PASS`.

The infinite Weierstrass product, all-exponent monotonicity, limiting non-Gaussian distribution, and asymptotic coefficient are analytical proof steps in `RESULT.md`, not conclusions from finitely many tests. The stochastic sampling validates only representative finite parameters and cannot prove convergence or global uniqueness. The cited stationary density is a known input and is explicitly attributed. Independent scientific validation has not been performed.
