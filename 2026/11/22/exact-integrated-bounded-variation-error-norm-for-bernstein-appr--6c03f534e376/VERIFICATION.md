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

Run `python3 checker.py` in a Python 3 environment. Exact rational polynomial integration checks the equality between step-error integrals, beta deviations and the closed binomial formula at degrees 1–16. Finite low-degree extrema are evaluated exactly. The code additionally checks seeded multijump inequalities and the numerical trend of the Gaussian constant; these are supplementary sanity checks rather than proofs of statements for every degree or every BV function. The universal proof uses the step decomposition, exact beta CDF, convexity, reflection, and beta central limit theorem with uniform integrability. Historical priority still requires full-text examination of Cheng (1983) and Bustamante et al. (2014). Independent audit has not been performed.
