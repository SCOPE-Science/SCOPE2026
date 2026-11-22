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

The standalone `check_faces.py` is deterministic and uses integer arithmetic. It enumerates the vertices of the canonical zonotope by all strict coordinate orderings, enumerates rank-two supporting objectives by every pair of graph edges and all distinct assignments of ranks to their equality components, deduplicates the exposed vertex sets, and computes each four-vertex parallelogram's squared area from its Gram determinant. It independently calculates the claimed counts by Stirling-number chromatic evaluation and compares the two complete histograms.

Command: `python3 check_faces.py`.

Observed cases: \((p,q)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)\), with areas squared in \(\{3,4\}\). The observed terminal line was `BICLIQUE_AREA_FACE_EXACT_PASS`.

This program is finite verification only. The all-parameter result is proved analytically using rank-two flats, acyclic orientations after contraction, and a dominant-term Stirling expansion. The program requires only Python 3 standard-library modules.
