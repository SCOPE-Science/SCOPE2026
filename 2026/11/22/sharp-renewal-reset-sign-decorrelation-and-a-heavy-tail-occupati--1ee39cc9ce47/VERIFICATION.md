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

The main conclusions are analytic: conditional sign persistence from the exact free last-zero Beta law, renewal age/residual averaging, convexity and Jensen, an exact integral identity, and regular-variation asymptotics. The complete proof is in `RESULT.md`.

Run `python verify.py` with NumPy and SciPy installed. On the reviewed script, checks passed: `poisson_gamma 12`, `deterministic_inequalities 350`, `power_law 32` (cumulative count including 12 prior checks; 20 distinct power-law comparisons), `integrated_correlation 6`, `free_last_zero 6`. These are bounded diagnostic comparisons, not exhaustive enumeration or substitutes for the proof. The script uses the formulas as written and independently numerical quadrature; no Monte Carlo sample establishes the theorem.

The stated asymptotics require equilibrium renewal initialization and a strictly positive finite mean reset interval. Critical and subcritical Pareto coefficients require the tail equivalence \(\Pr(W>t)\sim ct^{-\beta}\). Neither a nonstationary-renewal analogue nor a distributional fluctuation limit has been verified. Independent audit and independent scientific validation have not been performed.
