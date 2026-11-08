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

# Reproducibility and verification

Run `python3 verify_truncated_octahedron.py` in a Python 3 environment; no nonstandard libraries are required.

A completed run returned:

`VERIFY_OK vertices=24 edges=36 facets=14 chambers=5 exact_crossing_classes=5 spherical_cones=3 quadratures=4 sample_normals=180000 P6=0.498450689918 P8=0.316108855580 P10=0.185440454502 max_sampling_deviation=0.001142879`

The code rederives vertices and edges and verifies the support-facet incidence. It uses exact rational arithmetic for five generic normal witnesses and for all corresponding edge-plane intersection vertices, independently verifies the three radical solid-angle expressions, and numerically integrates the spherical normal density by a separate method. A fixed-seed Gaussian-normal simulation compares the predicted law with 180,000 orientations. All quantitative checks passed. The proof additionally supplies an all-direction chamber argument, which is necessary because finite sampling is not an infinite proof. The use of the solid-angle identity is elementary and analytically justified; no external numerical certificate is assumed. The exact theorem does not establish statistical confidence intervals.
