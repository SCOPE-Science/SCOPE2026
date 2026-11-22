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
The standard-library Python program `check_tetrahedra.py` exhaustively evaluates all \(495\) vertex quadruples using the signed Leibniz determinant expansion. It checks the spectrum, eight distinct constant-volume facial families, single 24-element symmetry orbit, and exact \(6/23\) capacity; its output is included as ordinary reproducibility only, not independent certification.

The theorem beyond the finite list is justified by the separate deterministic affine-extreme-point reduction: any contained tetrahedron can be moved vertex-by-vertex to a vertex-supported tetrahedron without decreasing absolute determinant. Since all four vertices are in a compact convex polyhedron, the maximum exists. Positive-dimensional optimizer families follow from equality of signed determinants at all three vertices of a triangular face. No classification of all nonvertex optimal families is asserted.
