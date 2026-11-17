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

Execute `python verify_pedal.py` with Python 3, NumPy and SciPy. The program was run against the complete packaged source and returned `PASS: 2865 finite checks, including actual n-step pedal simulations`.

It compares both independent numerical representations of the full scale: (1) the literal product of distances from a point to all supporting side lines divided by its product of distances to the original vertices, and (2) the Chebyshev closed formula; it also computes the actual sequence of perpendicular-foot polygons and checks the final edge-length scale. Multiple polygon orders from 3 through 31 and both inner and near-boundary radial points are covered. Monotonicity, exact endpoint formulas, and the angular gap are checked numerically. At extremely small radial scales, the strictly positive angular difference can fall below binary64 resolution, so no false floating-point separation is demanded in that regime.

The symbolic Chebyshev root identity, strict derivative argument, cross-section geometry, and uniform asymptotic expansion appear in `RESULT.md` and establish the all-integer, all-angle conclusions analytically. Numerics alone do not establish a universal theorem. The connection to an actual similarity uses the nondegeneracy assumptions of the cited prior iteration formula. Independent audit has not been performed.
