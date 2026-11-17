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

The reproducible verifier constructs all augmented faces and each directed Morse Hasse graph afresh. It separately checks the forbidden-distance identity for all ordered vertex pairs, total face counts, dimensions of unmatched faces, perfect pair accounting, and exhaustiveness of a directed topological sort. Exact output is included as `verification_output.txt`. The finite input has 25 torus vertices, and the proof makes no claim for larger grids or multiple punctures.
