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

# Verification and scope

The standalone `verify.py` is executable with Python 3 and uses only its standard library. It constructs all subgroup-orbit complexes directly from cycle vertices, independently compares those complexes with the closed formulas for all cycle sizes 3 through 28, checks all elementary pairing rules for folded intervals of lengths 2 through 15, explicitly checks directed acyclicity for lengths 2 through 12, and computes reduced mod-two Betti numbers independently for lengths 2 through 11. The exact program output is in `verify_output.txt`; running the program produces `ALL_DIHEDRAL_SUBGROUP_TWO_INDEPENDENCE_FIXED_MODELS_OK` on success.

The unrestricted result is established by the barycentric fixed-orbit lemma, quotient-and-folding description, explicit free-face collapse ordering, and the published ordinary cycle homotopy theorem. Neither a finite calculation nor a program execution proves the infinite family independently of those arguments. There is no independent audit or external mathematical certification.
