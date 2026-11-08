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

The included standard-library Python 3 checker `verify.py` was executed. It returned `VERIFY_OK exact_matrix_and_return_checks= 110 q_integers=3..9 pressure_q=10,20,40,80`. Its exact rational checks include stationary Markov vectors, characteristic-polynomial equalities at enough integer points to establish identities for each tested degree, and each first-return subinterval for parameters 3 through 9. Numerical Perron-root comparisons cover 10, 20, 40, and 80.

The all-integer invariant law and the all-real tilt pressure and asymptotic claims are proved analytically in `RESULT.md`, not inferred from finite checks. The classical renewal counting CLT is invoked after demonstrating genuine independent identically distributed bounded return times. Explicitly, the asymptotic variance is the variance of the waiting time divided by the cube of its mean. The supplied checker does not perform independent external scientific validation.
