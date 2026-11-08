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

This package provides `verify_cubic_census.py` and `verify_explicit_tangents.py`, executable with Python 3 and no external libraries. Run them from their containing directory. Both were run successfully and report `F7_TANGENT_FILLING_CUBIC_CENSUS_PASS` and `F7_EXPLICIT_CUBIC_TANGENT_FILLING_PASS` respectively. The first loops over all 42 smooth short Weierstrass parameters and all 336 degree-three divisor classes, checks each rational curve-point gradient and tangent coverage, and identifies eight covering normal forms. It asserts the full coverage histogram and exceptional list. The second independently encodes the explicit cubic, exact derivatives, twelve tangent lines and 57 ambient points, confirming incidence counts `1:36, 2:9, 3:9, 5:3`.

The completeness claim is not established by a finite search alone: it follows from the smooth cubic/elliptic curve identification, the rational degree-three Picard classes and the explicit linear series formulas proved in RESULT.md. The external standard theorems are the Hasse bound and basic elliptic line bundle properties. Proof of geometric smoothness of the explicit representative is symbolic and works over the algebraic closure. The scripts do not classify singular cubics, extension fields, or priority in literature. Independent audit or validation: not performed.
