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

# Reproduction and verification

The analytic proof establishes the exact diametral-pair set, the nondegenerate transverse distance expansion, the arclength-density Jacobian, the Hellinger identity and circle equality case, and the full-range support-function construction.

Run `python verify_constant_width_tail.py` in Python 3 with NumPy and SciPy. The program constructs boundary coordinates directly from support functions, numerically differentiates the chord deficit, solves the finite-threshold angular contact equations, analytically integrates one curvature-density factor, and compares the independent quadrature to the closed leading coefficient. Its observed success output was `CONSTANT_WIDTH_HELLINGER_TAIL_CHECKS_OK 79`.

The checker evaluates only the explicit threefold harmonic family and finitely many thresholds, not all positive-curvature curves, not the sharp lower-infimum construction, and not historical originality. Those claims rely on the proof and source comparisons in the accompanying mathematical record, respectively. All stochastic probabilities are population values, and the finite-threshold calculation is deterministic numerical integration, not a Monte Carlo or proof of a uniform asymptotic theorem.
