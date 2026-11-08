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

# Reproduction and limits

The exact sampled-data recurrence, companion matrices, quadratic Floquet polynomial, strict Jury inequalities, and global spectral-radius lower bound are proved in `RESULT.md`. These deductions establish the continuous parameter ranges; they do not rely on finite enumeration.

Run `python verify.py` in an environment satisfying `requirements.txt`. The supplied `verify_output.txt` records 2,809 assertions from a successful execution. These include symbolic identities, a rational two-interval example, a grid comparison between direct eigenvalue moduli and Jury inequalities, and numerical checks of the optimal lower bound. Random or finite checks do not prove an infinite-domain theorem, replace inspection of the proof, or certify publication precedence.

The calculation assumes exact arithmetic and noiseless delayed measurements. Transient peak gains, nonlinear dynamics, and arbitrary aperiodic sampling are not covered. The mean-period upper limit is a strict supremum, not a stable design point. At the optimal repeated Floquet eigenvalue the matrix is defective, so a polynomial prefactor can occur in matrix powers.
