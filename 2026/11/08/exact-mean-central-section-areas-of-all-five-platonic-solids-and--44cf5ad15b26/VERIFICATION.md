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
# Reproduction and limitations

`check_sections.py` constructs all five polyhedral vertex sets from unit-edge coordinates and checks their face supporting distances. For each solid it tests the exact polar face integral against adaptive quadrature and estimates the central section mean by actual clipping of 1,200 uniform-normal planes, with reproducible pseudorandom seed 3712. All five separate tests returned `CENTRAL_PLATONIC_SECTION_CHECKS_OK`. These sampling tests are not a proof of the continuous angular integral.

`check_intervals.py` evaluates the closed expression in 65 decimal digits of outward-rounded `mpmath.iv` real interval arithmetic, verifies five explicit separated rational open brackets, and returns `CERTIFIED_STRICT_NORMALIZED_ORDER_OK`. Independent reproducibility depends on the documented `mpmath` interval implementation. Its finite numeric comparisons supplement an exact analytic formula.

Theoretical justifications are fully given in `RESULT.md`: spherical Radon averaging, punctured divergence theorem, exact regular-face integration, known elementary unit-edge inradius formulas. They require no external symbolic or numerical execution.
