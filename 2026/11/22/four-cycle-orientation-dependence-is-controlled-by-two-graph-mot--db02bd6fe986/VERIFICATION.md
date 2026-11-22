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

The independent-orientation calculation is proved for every finite simple graph in RESULT.md. For reproduction with Python 3.9 or newer, run `python3 verify.py` in the directory containing this document.

The checker exhausts orientations of every four- and five-vertex labelled graph containing a four-cycle (486 graphs), and checks each exact covariance and the full variance identity. It also examines every orientation of the six-vertex complete graph and all 4096 orientations of the three-dimensional cube. The three cube faces through a specified vertex occur separately 512 times each, in pairs 64 times each, and jointly zero times.

The checker is finite evidence, not a replacement for the all-graph proof. There is no independent audit. Earlier literature might contain an equivalent arbitrary-graph covariance identity not indexed in available databases.
