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

# Verification

`python verify_capsule.py` from this package returned `CAPSULE_SURFACE_DIAMETER_CROSSOVER_CHECKS_OK 35` using NumPy. The checker compares exact Cartesian cap pair distances integrated over spherical angular coordinates with the claimed fixed-\(a\) coefficient and crossover function. It separately checks scale behavior, endpoint reconstruction and regularity at the crossover. The angular integration is independent of the local quadratic deficit proof. Its 35 finite checks do not exhaust infinitely many parameter values.

The formal argument lies in `RESULT.md`: unique poles for positive segment length; exact cap normal coordinates and quartic Taylor remainder; four-dimensional ellipsoid sublevel volume; spherical dot-product law; moving-parameter angular cap integration with negligible cylindrical mass; direct integration of the crossover. These are the critical logical dependencies. The uniformity of the positive-\(a\) remainder as \(a\downarrow0\) and the \(\lambda	o\infty\) simultaneous regime have **not** been proved. Independent proof review has not been performed.
