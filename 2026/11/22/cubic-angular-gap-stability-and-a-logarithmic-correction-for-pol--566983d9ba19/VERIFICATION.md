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

## Reproducibility

Run `python verify_chord.py` with Python 3 and NumPy. The checker integrates the original Euclidean segment-pair distance expression directly. For regular polygons, every same-edge contribution is the exact expected distance of two independent uniform segment points; cross-edge double integrals are computed by tensor Gaussian quadrature. For nonuniform polygons, it computes each pair of distinct segment integrals with arclength weights and exact same-edge terms.

## Actual checks

The verifier completed successfully on regular polygons with 20, 40, 80, 160 and 320 sides, plus sinusoidally modulated gap lists with 12, 20, 40 and 80 sides. The logarithm-corrected residual is approximately -0.281249 at 20 sides, -0.278328 at 40, -0.277476 at 80, -0.277232 at 160 and -0.277163 at 320. The nonuniform relative deviations from the cubic prediction are -0.021687, -0.008343, -0.002277 and -0.000618. All programmed assertions passed. Further internal mathematical checks: the radial-distance formula follows from a chord line equation, the arclength density integrates to one, the per-edge third-order integral is exactly -2/3 times the cube of the half-gap at leading order, and the regular radial-profile variance is one-forty-fifth times the fourth power of the half-gap.

## Limits

Numerical quadrature is approximate; it provides reproducibility and an independent stress test, not certification of any infinite asymptotic. The analytic bounds and periodic zero-mean lemma in RESULT.md establish the limits. No independent mathematical audit has been performed.
