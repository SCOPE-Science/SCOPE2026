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

The standalone `verify.py` runs under Python 3 with no external dependencies. It exhaustively generates exactly 399 nonempty faces, computes six exact binary boundary ranks in both row and column orientations, checks the reduced Betti vectors of the theta nerve and the union of its two constituent-cycle nerves, and verifies the claimed inclusion. All checks completed successfully on the supplied source. Exhaustive finite arithmetic proves only the specified finite instance, not an unbounded family; no integral torsion or homotopy type is certified.
