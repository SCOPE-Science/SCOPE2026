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

# Verification and reproducibility

Run `python verify_antiprism_law.py` with Python 3, NumPy and SciPy. Output obtained from the embedded file:

```
ANTIPRISM_TAIL_VERIFIED 550 assertions; sample coefficients: [(3, 3.30797337), (4, 4.34711172), (5, 6.05461383), (8, 13.85680107), (12, 30.03713405)]
```

The checker compares analytical facet planes with independently reconstructed convex hull facets for eight polygon orders. It computes the last uncovered gaps by a longitude-integrated area of spherical-height intervals (rather than by the latitude formula), tests 32 angular deficits, and independently counts exact 3D dot-product cap memberships for 468 latitude/radius/height examples. This includes three distinct nonoptimal heights and radii on either side of a hemisphere. It also confirms the previously known six- and eight-site constants. These finite numerical checks neither establish infinite-order correctness nor historical novelty; the mathematical proof and separate prior-work analysis supply those arguments. The stated theorem only concerns fixed spherical sites, independently uniform sample directions, and the parameter ranges in RESULT.md.
