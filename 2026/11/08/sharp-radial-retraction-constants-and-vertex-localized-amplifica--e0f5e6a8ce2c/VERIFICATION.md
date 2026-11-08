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
# Verification and limits

The reproducible standalone `verify_regular_polygon_radial.py` constructs all supporting functionals of each even regular polygon of side count from four through 120, checks the exact induced rank-one maps at seven positions on each reference facet (413 evaluations), and tests the vertex-localization deficit for side counts divisible by four. It also constructs 15 exterior pairs approaching the predicted sharp derivative. It prints `ALL_REGULAR_POLYGON_RADIAL_DIAGNOSTICS_PASSED` on success. The script was run successfully against the actual embedded package; output and integrity were checked separately.

This is finite numerical corroboration, not a proof for all side counts. The symbolic proof is in RESULT.md, Sections 1--4. In particular, the exact identity from determinants, support-functional geometry and strict convex endpoint argument are essential; the diagnostics cannot establish nonattainment for arbitrary pairs. Independent mathematical audit has not been performed.
