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

The supplied `checker.py` reconstructs the two finite witnesses from specified edge rules, tests exact common-neighbor counts, and checks every induced subset up to the relevant rank in the \(12\)- and \(36\)-vertex cases. It was executed against these exact package bytes and returned `ALL_FAREY_BOUNDARY_CHECKS_OK`.

The universal degree inequality follows from an explicit neighborhood/link argument; the orientable-genus estimate uses Euler's edge inequality. For arbitrary \(m\ge6\), the absence of short induced cycles in the triangular torus graph is proved via lifting to the planar triangular lattice and the disk Euler degree identity. The computations neither certify the universal argument by exhaustive enumeration nor establish any unknown optimal higher-genus threshold.
