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

The result is established analytically by conditioning, uniform gamma survival asymptotics, the modified-Bessel integral and a strict saddle-point localization argument. The exact positive-integer-shape finite Bessel expansion provides a separate way to evaluate the joint probability at finite thresholds.

The standalone script `verify.py` uses `scipy` and checks the integral against the finite Bessel sum, checks representative large-threshold asymptotic ratios for both unequal and equal directions, and checks moments of an exactly identified generalized-inverse-Gaussian conditional law. Run `python verify.py` after installing the dependency specified in `requirements.txt`.

Finite numerical checks do not prove the unbounded-threshold limits. The proof assumes a fixed positive-dimensional parameter vector, and no historical-priority certification is represented by these computations.
