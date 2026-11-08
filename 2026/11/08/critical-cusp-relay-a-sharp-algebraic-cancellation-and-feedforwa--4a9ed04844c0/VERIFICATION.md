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

Run `python verify_relay.py` with Python 3, NumPy, and SciPy. It checks representative numerical terminal and relay trajectories at multiple observation horizons against the proof's exact leading coefficients and signed integral; the source file embeds all initial values and tolerances. It also checks exact cancellation and the time-shift identity. Observed terminal output: `VERIFY_OK critical_relay=1 symmetric_exact=1 signed_quadrature=1 balanced_samples=3 unbalanced_samples=6 time_shift_samples=2 crossover_samples=6`.

Analytical proof components are the exact logistic normalization, autonomous scalar time-translation identity, the cubic damping limit, and stable-kernel asymptotics. The numerical code cannot certify the universal asymptotics or historical priority. The parameter-dependent crossover has been independently spot-checked for fixed scaled imbalances; its proof is in `RESULT.md`.
