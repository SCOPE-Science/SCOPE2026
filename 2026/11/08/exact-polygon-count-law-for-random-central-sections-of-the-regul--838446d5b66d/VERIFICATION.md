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

The exact proof relies on the integer-coordinate construction, the complete arrangement of twelve vertex-normal great circles, and spherical excess; it does not rely on Monte Carlo sampling. The standalone program `verify_truncated_tetrahedron.py` enumerates vertices of the half-space model by rational linear algebra and checks all 220 triple determinants, all 134 distinct sign chambers, 132 crossing points, 528 corner incidences and the angle multiplicity table. It recomputes all three probabilities and the independent expected section-vertex identity. A seeded simulation of 180000 normals is supplementary only.

Reproduce with `python3 verify_truncated_tetrahedron.py`. The only dependency is Python 3's standard library. The accepted theorem is the exact three-point distribution for **central**, not arbitrary affine, slicing. Independent validation and historical-priority review are not performed.
