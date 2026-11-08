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

# Verification of centroidal radial moment inverse

Run `python3 check_radial.py` using the Python 3 standard library. It exactly expands the barycentric polynomial for squared distance and checks every coefficient after integrating barycentric variables using the factorial moment identity. Its expected output is:

`VERIFY_OK universal_polynomial_identities=3 exact_triangle_cases=201 sharp_two_moment_pair=1 exact_area_formula=checked`

The checker additionally verifies elimination of the three symmetric elementary functions for 201 exact positive-area squared-side triples and both explicit two-moment witnesses. These are exact finite algebraic validations of the stated identities, not a claimed exhaustive enumeration of arbitrary triangles or independent certification. The mathematical proof establishes the universal inverse using symmetric-polynomial identities and the side-side-side criterion.

The third-party historical-priority check is incomplete because the full older literature is not exhaustively accessible. No noise-stability bound has been proved.
