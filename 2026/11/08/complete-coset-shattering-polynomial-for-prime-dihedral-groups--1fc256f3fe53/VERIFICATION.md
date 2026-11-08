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

# Reproduction and scope

Run `python3 verify_dihedral.py` with Python 3.9 or newer and the standard library only. For each odd prime in \(\{3,5,7,11\}\), the checker generates the order-\(2p\) semidirect product multiplication, constructs all one-/two-generated subgroups, forms all distinct left cosets, enumerates traces on every support of sizes zero through three, and independently compares the coefficient and concept-count formulas.

The run reported `ALL_DIHEDRAL_COSET_SHATTERING_CHECKS_PASS` after four exact parameter tests. The correctness of the universal polynomial follows from the proof in `RESULT.md`, including the separate four-point obstruction; finite enumeration is only corroboration. The checker does not attempt a complete scan of all academic publications or provide independent audit. The group calculation assumes the standard semidirect-product presentation for an odd prime.
