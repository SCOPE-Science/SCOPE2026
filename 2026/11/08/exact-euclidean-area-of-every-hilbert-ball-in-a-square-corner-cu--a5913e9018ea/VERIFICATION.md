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

The exact proof is in `RESULT.md`. The standalone geometry check is `check_area.py` (Python 3.9+, standard library). Executing `python check_area.py` returned `HILBERT_SQUARE_EUCLIDEAN_AREA_OK 350`. Its separate checks compare 150 line-intersection cross ratios with the facet ratio expression, construct 350 radius balls directly from 12 half-planes, compute areas by the shoelace formula, check the square-center limit and coordinate-axis second variation, and verify the 4/6/8 vertex cases.

No finite numerical sweep is asserted as an exhaustive theorem; the all-center/all-radius argument is algebraic. The proof's exact limits are interior centers, finite strictly positive unhalved Hilbert radii, ordinary Lebesgue area and affine images of the square. Independent mathematical and historical checks have not been performed.
