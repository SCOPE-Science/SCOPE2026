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

Run `python3 verify.py` using Python 3 with no third-party dependencies. The checker performs exact integer-pair algebra in \(\mathbb Z[\varphi]\), where \(\varphi^2=\varphi+1\), derives the vertex-edge-facet structure, enumerates all normal-sign chamber incidences and their angle types, and checks the precise 20/60/12 chamber profiles. A separate independent projected-convex-hull sampler uses 36,000 random viewing directions; it corroborates rather than proves the exact Haar probabilities.

The expected terminal labels are `EXACT_ICOSAHEDRON_SHADOW_TYPE_CERTIFICATE_OK` and `INDEPENDENT_ORTHOGONAL_PROJECTION_HULL_TEST_OK`. Every asserted exact count is validated by ordinary Python assertions on exact algebraic integers; numerical operations occur only in the final probability evaluation and independent finite simulation. No third-party certificates or independent audit are asserted.
