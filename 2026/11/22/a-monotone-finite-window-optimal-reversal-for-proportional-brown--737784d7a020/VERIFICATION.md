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

The standalone `checker.py` was run with Python 3, NumPy and SciPy. It passed 83 checks: exact weighted-integral optimum versus independently optimized finite-horizon variance at 11 durations, the strict root interval and monotonicity, small- and large-window expansions, 32 independent symbolic-formula comparisons, and finite Monte Carlo validation at four signed multipliers. The stochastic tests used 88,000 separately generated stationary paths with Gaussian-bridge integration between Poisson jumps, agreeing with the analytic variance within the stated 9% check tolerance.

The proof of the continuum statement is the explicit positive Laplace-weight optimization and its monotone-likelihood-ratio comparison, not the numerical tests. The claim has not received an independent scientific audit. The finite-sample computations do not certify priority or correctness beyond the tested cases.
