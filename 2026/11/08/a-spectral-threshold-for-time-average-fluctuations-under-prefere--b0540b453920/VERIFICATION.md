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

# Verification of the spectral time-average law

Run `python3 verify.py` with standard Python 3; no external modules or downloads are needed. The replay compares a high-precision finite-time power-series evaluation with direct Runge–Kutta integration of the differentially derived moment system for six parameter combinations. It checks the exact no-reset stationary Ornstein–Uhlenbeck formula. Finally, a seeded finite-grid simulation of uniform-past history relocations tests three nonzero relocation rates against the analytic finite-time variance.

The delivered execution passed all 16 comparison assertions. Simulated relative discrepancies for rates \(0.25\), \(1\) and \(2\) with unit stiffness and diffusivity, at time \(6\), were approximately \(1.45\%\), \(2.00\%\) and \(3.45\%\). Simulation has finite grid and finite sample error. This program does not certify the infinite-time theorem; the proof is in `RESULT.md`.

The result's scope excludes non-eigenfunction observables, nonequilibrium initialization, higher cumulants and limiting distributions. Independent scientific audit has not been performed.
