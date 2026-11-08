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

# Verification record

The exact proof is in `RESULT.md`. A standalone standard-library checker `geometry_droot_checker.py` enumerates signed two-support vertices and root-graph edges using integer scalar products. For each original facet it determines precisely which crossing edges lie within that facet. It verifies the two stated section-face counts for dimensions \(4,5,6,7\) at two independent ordered normal vectors.

Observed dimension/count pairs: \((4,32,18)\), \((5,80,36)\), \((6,160,70)\), and \((7,280,136)\). In dimension four, the facet-size spectrum is six quadrilaterals and twelve hexagons; all 32 section vertices have degree three, the section has 48 edges, and the quadrilateral adjacency induced through hexagons is \(K_{2,2,2}\).

Run `python3 geometry_droot_checker.py`. It prints `D_ROOT_GENERIC_SECTION_EXACT_COUNTS_OK` on successful completion.

**Limits:** The finite computation tests only the listed dimensions and normals, while the text proof covers all dimensions and every generic normal. There is no independent audit or certification, and literature priority remains provisional.
