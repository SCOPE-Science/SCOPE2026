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

The exact planar annulus formula is proved analytically in RESULT.md using the scaled-unitary symmetric/skew decomposition, Takagi factorization, the two-dimensional orthogonal decomposition, and one-variable extrema.

The standalone diagnostic is `checker.py` and uses only the Python standard library. It was executed as `python3 checker.py` and returned:

`TWO_DIMENSIONAL_ANTILINEAR_Q_RANGE_FINITE_OK 475146`

The 475,146 finite assertions check inner-product identities, the scaled-isometry property, the range inclusions for sampled constrained pairs, and dense angular approximations to both exact radius formulas for seven canonical operators and nine overlap parameters. These calculations are a consistency check, not an exhaustive verification of a continuum or a proof of the stated theorem.

The paper's online Section 6 and the relevant earlier ordinary-numerical-range literature were inspected. The original source establishes annular shape and a special obstruction in dimension two; the radius formulas for the full planar scaled-antiunitary family are the claim here. No independent verification or publication-priority certification is asserted.
