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

# Reproducibility and limitations

The proof in `RESULT.md` is analytic and does not require a computational certificate. A direct independent evaluation of the secant-slope angular identity gives \(0\le\dot\theta\le\sqrt{AB}\). This bound, the direction of crossing, and the simple zero of the logistic linearization are the critical mathematical steps.

The included standard-library `CHECK.py` was run from this package. It checked sixteen strictly precritical observation times across four logistic initial separations, bracketed first postcritical zeros, and verified exact-plateau vector-field identities at 129 times for four amplitudes. The resulting first equality times, decreasing towards \(4\pi\), were approximately 12.57798351, 12.56709827, 12.56640018, and 12.56637157. All checks passed.

The sampled equality of the plateau construction for all nonnegative integers follows exactly from its closed-form solution, not from floating-point observations. The code verifies the closed-form solution against the piecewise regulatory vector field over a finite test grid, not for every real time. It does not certify historical priority, generalize the result beyond its hypotheses, or constitute independent mathematical validation.
