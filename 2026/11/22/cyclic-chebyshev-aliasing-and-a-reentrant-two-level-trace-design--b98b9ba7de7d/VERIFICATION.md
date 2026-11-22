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

# Reproducibility and boundaries

Run `python verify.py` from this package with the `sympy` dependency declared in `requirements.txt`. The verifier checks the exact algebraic elimination polynomial, exact Sturm root counts in the rational isolating intervals, the sign rejection of two extraneous roots, the two accepted numerical root approximations, cycle Chebyshev recurrences and Rademacher covariances through size eight, and independently enumerated sign-vector variances through size seven.

The all-size covariance identity and exact phase classification are proved in `RESULT.md`, not inferred from finitely many checks. The work-variance frontier uses positive real allocations with costs proportional to standard **one-sided** Chebyshev recurrence degrees; it does not certify optimality for integral sample budgets, faster two-sided evaluation, implementation-aware simplifications, or broader matrix classes. Publication priority and independent mathematical validation remain outstanding.
