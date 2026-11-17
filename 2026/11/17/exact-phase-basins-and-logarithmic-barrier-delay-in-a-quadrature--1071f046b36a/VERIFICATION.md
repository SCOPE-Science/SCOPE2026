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

Exact reductions can be checked directly from the equations in arXiv:2209.10514 by setting \(\omega=0\), \(\alpha=\beta=\pi/2\) and defining mean/difference couplings. The proof supplies the coercive energy identity, phase-barrier invariance, integration of dissipation, uniform first-entrance bounds and the local relaxation characteristic polynomial. These establish statements for all admissible initial conditions and arbitrary positive \(a,\varepsilon\).

Execute `python checker.py` with Python 3, NumPy, SciPy and SymPy. Its source is included. It checks exact symbolic reductions and the energy derivative, compares integrated full and reduced systems for sixteen parameter/initial-state choices, verifies the energy budget by quadrature, and checks numerically the phase-barrier delay slope and the focus/node behavior on selected finite trajectories. These finite checks do not constitute proofs of infinite-time behavior or exhaustive parameter verification.

Unproved extensions include robustness under detuning, general interaction/learning lags, arbitrary network size and noise. Publication priority may depend on unindexed equivalent results; independent auditing has not occurred.
