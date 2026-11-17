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

# Verification of the periodic mean-bias law

Run `python verify.py` from the directory containing `verify.py`, with dependencies in `requirements.txt` installed. The script checks the odd-response Taylor coefficients, the quadratic oscillator's constant and second harmonics, the cubic environmental-moment coefficient, and the Fermi specialization using symbolic algebra. It also performs eighteen finite integrations of exactly specified periodic trajectories, locating full periods by a downward logit-coordinate crossing. The tested families cover both signs of environmental asymmetry, two nonlinear response shapes with opposite cubic curvature, differing environmental response speeds, and the exactly symmetric environment.

The reported numerical period, half-range and mean estimates are computed from the current packaged equations and code, not from a retained execution log. Finite numerical integration cannot certify every periodic orbit or an asymptotic remainder; the analytical proof in `RESULT.md` establishes those statements. The source's generic payoff-dependent model and nonlocal finite-amplitude bias sign are outside the scope. No external independent validation has been performed.
