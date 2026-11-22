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

# Reproducible checks and boundaries

Run `python verify.py` using the standard Python library; no network or nonstandard packages are required. The program builds exact rational positive-definite two-level matrices using an explicit rational orthogonal reflection, verifies their inverses and the actual Hermite residual, exhausts every Rademacher sign vector for dimensions two through eight at 84 exact matrix/parameter configurations, and checks the unbiasedness and variance relation using exact fractions.

Observed output: `VERIFY_OK | 84 exact matrix families | 8184 exhaustive sign-vector comparisons`.

The universal theorem rests on the analytic two-level identity \(A=(a+b)I-abA^{-1}\), not on the finite enumeration. In particular, finite checking cannot establish the statement for all matrix sizes, all eigenbases, real contrasts, or arbitrary probe budgets. The additional seventh-dimensional endpoints are verified as rational identities. These checks use exact inverse products and do not assess floating-point error, runtime, or independent mathematical audit.
