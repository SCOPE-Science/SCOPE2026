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

The theorem follows from published deterministic Schur stability plus an exact Yule--Walker derivation for the cubic recurrence, direct endpoint asymptotics, and an independent quadratic minimax and stationary-variance derivation for delayed gradient descent. The supporting checker `checks/check.py` can be run using Python 3, NumPy, SciPy and SymPy. It provides 450 numerical/Lyapunov/simulation diagnostics and nine separate exact-rational Yule--Walker checks. These checks supplement rather than replace the infinite-parameter analytic proof. No external audit or independent validation has been performed.
