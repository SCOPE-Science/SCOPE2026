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

# Reproducibility and scope

Run `python3 prism_exact_verifier.py` in the extracted directory. The script requires only the Python standard library, constructs planar difference-body convex hulls with exact integer cross products, and enumerates all unordered pairs of both prism vertices and prism edge midpoints. It verifies the formulas for 187 test polygons (seven fixed, 180 deterministic pseudorandom hulls). Expected terminal marker: `PRISM_ANTIPODAL_EXACT_OK 187`. These computations test only the displayed integer configurations. The all-parameter proof in `RESULT.md` does not depend on test coverage.

The main external source's abstract, a detailed openly available scientific synopsis and its examples were compared to the result. A page-by-page full-text priority comparison could not be completed because the primary HTML/PDF and institutional access were unavailable; no independent audit has been carried out. This is a limitation of originality assessment, not a computational certificate of novelty.
