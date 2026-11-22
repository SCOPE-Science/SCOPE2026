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

# Mathematical and computational checks

The proof reduces the transverse exponent to a logarithmic moment of a bounded iid sample mean. The two-dimensional double-sine integral is evaluated by Abel-regularized Fourier series, and the high-dimensional coefficients are derived from the exact first three centered moments, fourth-moment pairing, and controlled Taylor remainder. The leave-one-out strict Jensen argument establishes monotonicity for every finite dimension and is not inferred from numerical samples.

Execute `python3 check_threshold.py` (Python standard library). The executed script reported `PASS: moments, dimension coefficients, odd Fourier sum, and 2D quadrature`, with the two-dimensional threshold near 1.705294057431. The tests check algebra, finite Fourier truncation, and deterministic numerical quadrature; the proof, not their finite bounds, supplies the infinite claims.

No formal verification or independent mathematical audit has been performed. For all \(d\), the result describes Haar-typical linear response at the invariant zero graph only. The nonlinear equality case and alternative invariant measures are outside scope.
