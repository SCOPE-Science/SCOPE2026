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

# Verification

Execute `python3 CHECK.py` using the Python standard library. A run during preparation printed `PASS: 1710 standalone exact/numeric assertions`.

The checker enumerates all four-category multinomial cells for several finite sample sizes and verifies the two-label marginal identity with exact rational arithmetic. It verifies the elementary first-future-hit linearization inequalities for several sample sizes, window lengths, record orders and rational atom masses. Numerical integration checks four Gamma-transformed intensity integrals, and finite-binomial Zipf intensity sums for two growing sample sizes check the predicted asymptotic constants.

The infinite claims are not verified by finite enumeration or floating-point checks. The rigorous argument is in `RESULT.md`, notably the uniform compact-rank multinomial covariance bound, integrable occupancy tails, the one-hit coupling and the conditional Laplace product expansion. The conditional rate only applies to bounded Lipschitz tests compactly supported in positive rank; no total-variation convergence to a continuous mark distribution is claimed. Priority against all potentially relevant older marked-process literature has not been independently determined.
