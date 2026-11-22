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

The exact proof uses the polygonal divergence-theorem expansion of the Fourier transform, a fixed-direction separation of parallel and transverse edges, Riemann–Lebesgue cancellation of separated parallel-edge cross terms, and an explicitly integrated sinc attenuation coefficient.

`check.py` executed successfully with Python 3 and `mpmath`. It compared four triangle Fourier values with direct numerical area integration (absolute discrepancies below \(10^{-55}\)), tested the exact triangle divided-difference spectral moment for seven decreasing angles, matched the independent square coefficient algebraically, compared the sinc integral with its gamma-function evaluation, and tested five successive angular scales of an asymmetric trapezoid with two unequal parallel edges using an exact projected-vertex spectral formula. The trapezoid coefficient converges to the predicted sum, with final relative error below \(2\times10^{-9}\).

A finite check of examples is not a proof of the all-polygon theorem. The analytic cross-edge remainder bounds are decisive. No formal proof assistant, external mathematical certification, or independent audit has been used.
