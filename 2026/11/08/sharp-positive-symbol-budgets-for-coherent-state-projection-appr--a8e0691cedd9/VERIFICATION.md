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

The exact analytic proof is in `RESULT.md`. The companion `verification.py` is standard-library-only and tests the integer Gamma identities and numerical stability of the balancing equation for the displayed finite set of dimensions and budgets. Running `python verification.py` produces `FOCK_POSITIVE_BUDGET_CHECK_OK 743 finite assertions`.

The program checks the candidate's vacuum/one-particle balancing equality and verifies that the remaining selected homogeneous-degree eigenvalues do not exceed the one-particle eigenvalue. These finite tests **do not** establish global optimality, uniqueness over nonradial symbols, or uniform asymptotics. Those rely on the exact two-moment lower bound, the bathtub equality case, and Gamma-density monotonicity proved in `RESULT.md`.

Symbols are restricted to measurable functions with values in the closed real interval \( [0,M] \). The high-budget rate is proved for each fixed positive integer dimension, not claimed uniformly in dimension. No independent mathematical audit was performed.
