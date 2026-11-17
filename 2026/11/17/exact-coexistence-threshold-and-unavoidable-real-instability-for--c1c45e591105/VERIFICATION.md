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

The proof reconstructs the actual delay equations, equilibrium denominators and the infected-history compatibility constraint. At the positive equilibrium, the Jacobian-at-zero determinant identity is shown by an explicit block Schur complement, not inferred from finite eigenvalue scans. A real positive zero follows by the intermediate value theorem and is compatible with the biological state space.

`CHECKER.py` carries out independent finite-parameter tests: direct construction of instantaneous and delayed characteristic matrices, root-finding of positive equilibria, evaluation of the sign identity, localization of a positive real characteristic exponent, and eigenvector compatibility. The examples include two distinct latency periods, three distinct latency periods, and a boundary case where surviving burst is exactly one. The checker requires the versions of NumPy and SciPy specified by `requirements.txt`.

The checker cannot establish the universal assertion, which follows from the analytic nullcline and determinant proof. The claimed novelty is conditional on accessible literature; no independent external scientific review has occurred.
