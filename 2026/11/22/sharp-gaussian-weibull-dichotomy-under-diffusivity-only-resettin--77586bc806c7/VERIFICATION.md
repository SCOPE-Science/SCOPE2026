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

The conditional-normal representation gives the second moment, fourth cumulant and Fourier-limit formula. A sharp fixed-time logarithmic tail follows from independent Laplace initial bath amplitude, the Brownian-supremum upper control, and a no-reset lower event. The deterministic-zero-bath transform cutoff follows from the Feynman–Kac Riccati solution and conditioning on Poisson excursion lengths.

Reproduce deterministic and simulation diagnostics with `python3 check.py` (NumPy and SciPy required). The checker does not evaluate an infinite-dimensional rare event by finite simulation; the rare-tail coefficient is proved by matching logarithmic upper and lower bounds. Its independent simulation is limited to a finite-step approximation of the integrated diffusivity; discrepancies from exact variance are stochastic and discretization effects. All fixed-time tail assertions apply to stationary bath initialization; the exact finite transform cutoff applies to zero-bath initialization. No independent external scientific audit has been performed.
