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

# Verification and limits

From the supplied directory, run `python check.py` with Python 3, NumPy and SciPy installed. In the checked environment it printed `PASS 403 deterministic assertions`. The program solves the continuous Lyapunov equation, evaluates exact bivariate block Gaussian KL divergences, checks the current and resonance formula for rotating and nonnormal drifts, and examines real-spectrum non-resonance and two-clock separation.

The numerical calculations use floating-point tolerances and a finite collection of parameters. They do **not** prove the exact assertions for every stable real matrix and positive-definite diffusion. The proof instead derives the general identity for the lag-current via Cayley–Hamilton; stationary Gaussian detailed balance and the analytic KL formula supply the necessary universal arguments. The proof concerns exact laws rather than finite-sample hypothesis testing. No separate external validation, experimental measurement or third-party scientific audit has occurred.
