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

Run `python3 verify_icosa_gp.py`. This uses only the Python standard library, with no external data or dependencies.

Checks: the labeled graph is five-regular with 12 vertices and 30 edges; its diameter is three with six antipodal pairs; all 220 graph triples and all 4096 vertex subsets are examined; 120 forbidden triples and the full face vector are obtained exactly; the distance-two core has 30 edges and 20 triangles and every link is a five-cycle; every original edge has a witness for a free triangle-edge pair; six antipodal edges are excluded from every triangle; and each of thirty tetrahedra has two uniquely incident triangular faces, giving a complete collapse certificate.

The verifier does not substitute a numerical calculation for the classical topological implications. The connected closed surface theorem gives the core two-sphere; attaching cells of dimension at least two preserves simple connectedness; elementary collapses preserve homotopy; and Hurewicz plus the simply connected homological Whitehead theorem yield the twenty-one two-sphere wedge. The six remaining one-cell attachments wedge on six circles. Independent audit: not performed.
