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

# Reproducibility and scope of verification

The analytic proof is self-contained in `RESULT.md`. Its critical points are the perpendicular displacement forced by equal antipodal edge lengths, cyclotomic closure, and the strict gap between a regular even polygon's antipodal and all other vertex distances.

`checker.py` was executed with Python 3 and SymPy. It passed 24 symbolic cyclotomic-divisibility tests and 24 floating-point convex small-polygon realizations for orders 6 through 70 as enumerated by the script. It also checked the exact dyadic cyclotomic identity at orders 4, 8, 16, 32, 64. The tests are finite examples and do not themselves establish the infinite-order classification. The proof does not establish any unrestricted local maximality for dyadic polygons, any large-displacement feasibility, or historical uniqueness among all mathematics publications.

Independent audit: not performed.
