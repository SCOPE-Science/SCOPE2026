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

# Verification details

Run `python3 check_bias_shift.py` using a Python 3 standard-library interpreter. The checker performs 2,209 finite assertions: exact `Fraction` tests of the shifted tail-ratio identity for five candidate periods and three Bessel indices, a strictly nonfixed two-cycle, finite-window convergence and its weight-sandwich TV bound, and high-precision tests of positive factorial-series tails.

The proof in `RESULT.md` is the verification of infinite-dimensional statements: its domination argument supplies total-variation continuity on the compact parameter space, the exact quadratic-weight cancellation proves conjugacy, and the symbolic-shift realization proves period/entropy/omega-limit statements. Numerical tests cannot certify the claims for all indices, all laws, or infinite time. The standalone code provides supporting diagnostics only; it is not an independent mathematical audit or a formal proof checker.

All assumptions and proof limits are explicitly documented. No external package or unbundled dataset is required.
