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

# Reproducibility and boundaries

`RESULT.md` contains the full analytic proof, including the renewal-reward reduction, the Mills-ratio sign argument, the strictly alternating Fourier-series concavity proof, and the strict Poisson comparison.

Run `python check.py` with Python 3 standard library. During preparation the program completed with `checks_passed: 528`, `theta_star: 0.0918903456528753`, and `max_Deff_over_D: 1.3324778873483827`.

The code checks two independent formulas for the same Gaussian-rounded second moment, sampled derivative signs, a numerical root interval, and the exponential-clock/Laplace closed formula. Grids, truncations, and floating-point evaluations are finite diagnostic evidence only; the proof of uniqueness for all positive intervals and the all-renewal ceiling is the analytic argument in `RESULT.md`.

No external independent scientific audit has been performed. No claim is made for interval distributions without a finite second moment, adaptive reset rules, irregular lattices, or finite-speed returns.
