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

The full finite-time factorization is proved by direct substitution and induction. Its exact Euclidean norm uses normality of the permutation matrix and its cycle Fourier modes. Both critical limits use finite-dimensional logarithm expansions with vanishing quadratic remainders.

The accompanying `verify.py` requires only Python 3. It compares 15 direct nonlinear steps at five parameter values with the independently iterated normalized-chain factorization, three finite-scaled times at four residue classes for the near-permutation limit, three finite-scaled times for the near-identity limit, and the sharp Fourier-mode spectral ratio for four parameters and three powers. It printed `EXACT_NONLINEAR_LINEAR_FACTORISATION_OK`, `BOTH_ENDPOINT_POISSON_WINDOWS_OK`, `SHARP_SPECTRAL_FACTOR_OK`, and `PERMUTATION_QUADRATIC_POISSON_VERIFICATION_OK` in an actual local execution.

The tests are finite checks only; the all-dimension spectral statement, exact formulas for all times, and the infinite-sequence critical limits follow from the written algebraic proof. The unavailable full text of a closely related 2023 paper remains an originality risk. Independent mathematical validation has not been performed.
