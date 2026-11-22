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

Run `python3 verify_tangent_rigidity.py` using Python 3 with SymPy. The script uses only finite binary operations and exact characteristic-two Gröbner bases. It verifies the complete 65,536-class rational Jacobian filter, all 288 survivors, the two 144-orbits, the geometric Jacobian status of both orbit representatives, the 288 incident point–line matchings, the exact 10,296-pair smooth tangent-agreement spectrum, the absence of a smooth third pencil member, and 36 octagonal eight-vertex components with four additional singular-orbit edges per component in the matching disjointness graph.

The scope is the fixed symplectic cubic over the binary field; finite-field checks do not prove any claim for larger fields. Smoothness over an algebraic closure is checked via unit ideals in every affine chart, not by bounded field-point searches. Historical uniqueness is not certified and independent mathematical audit was not performed.
