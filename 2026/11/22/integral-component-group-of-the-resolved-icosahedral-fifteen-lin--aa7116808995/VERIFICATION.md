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

# Reproduction

Run `python3 verify_icosahedral_boundary.py` with Python 3.9 or later and no third-party packages. The script uses exact rational pairs in the quadratic field, not floating-point approximations. It reconstructs every line and all 105 pairs, verifies the intersection multiplicity census and stable graph sizes, and computes its Laplacian directly from the edge list. It then independently calculates two reduced determinants and the entire characteristic polynomial and checks prime-local ranks at 11, 17 and 31. The Smith factors follow from determinant valuations equal to modular nullities. Its expected completion marker is `ICOSAHEDRAL_15_LINE_STABLE_BOUNDARY_INTEGRAL_GROUP_OK`.

The mathematical verification proves the finite incidence and integral matrix claims by exhaustive, exact computations. The identification of the critical group with a geometric Néron component group is conditional on the standard regular semistable hypothesis stated in the result, and is not established from the script. It is not an assertion about models with different thicknesses, the surface Picard group, historical uniqueness, or any independent review.
