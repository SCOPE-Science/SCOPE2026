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

# Verification of the shear convex-order theorem

`verify.py` is standalone and uses only the Python standard library. Run `python verify.py` in the same directory as `RESULT.md`. It exactly integrates the second and fourth moments under six rational parameter choices for each of the area and boundary laws and independently crosschecks the sharp curvature coefficients. It also performs deterministic numerical quadrature tests for the moment-exponent reversal.

The recorded output is `SHEAR_CONVEX_ORDER_CHECK_OK exact_pair_moments=12 sample_power_tests=3 strong_curvature_coefficients=exact`. The analytic proof in `RESULT.md`, not the finite arithmetic tests, establishes every quantifier over all positive side lengths and all admissible shear angles. The strictness depends on the nonzero-probability cross term. Historical uniqueness and independent audit are not established.
