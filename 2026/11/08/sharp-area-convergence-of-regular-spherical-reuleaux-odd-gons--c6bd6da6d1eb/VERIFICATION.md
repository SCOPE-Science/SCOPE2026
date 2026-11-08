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
# Verification details

From the contained `verify.py`, run `python verify.py` in an environment with `mpmath`, `sympy`, and `numpy`.

The actual run returned:

`VERIFY_OK symbolic_third_derivative=1 strict_normalized_cases=212 spherical_arc_cases=12 endpoint_cases=5 monte_carlo_orientation_samples=960000 max_area_deviation=0.00805753`

The script checks the analytic third derivative symbolically, 212 high-precision geometric and normalized-inequality instances, 12 independently reconstructed spherical arc angles, the previously known hemispherical-width area formula at five odd corner counts, and 960,000 independent uniform-sphere points across four spherical disk intersections. All finite computations are consistency checks. The all-width and all-odd-corner results are proved using spherical trigonometry, Gauss–Bonnet, a positive derivative, and the integral Taylor remainder in `RESULT.md`.

The exact differential inequality and all nontrivial limiting steps have been reconstructed by mathematical proof; no infinite assertion depends on an incomplete numerical search. The old inaccessible historical paper affects priority risk, not the analytic proof. Independent scholarly checking is not represented by this document.
