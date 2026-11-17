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

The independently executable `checks/theta_cycle_verify.py` enumerates independent faces of cycles of lengths 4 through 18 and tests signed augmented Lefschetz traces on all 330 rotations and reflections without using the orbit-graph formulas. It also directly enumerates noncover faces and computes signed traces for all 170 group elements at lengths 4 through 13, without using Alexander duality. The checks are compared to the exact all-length character theorem. In lengths 4 through 13, it also calculates boundary ranks over three different prime fields using sparse exact elimination. The original standalone script executed to completion and wrote `checks/theta_cycle_verify_output.txt`. The final marker is `NONCOVER_CYCLE_DIHEDRAL_CHARACTER_PASS`.

These finite confirmations do not by themselves establish the all-length result. The general proof is a signed orbit-graph count plus equivariant Alexander duality and the classical Kozlov cycle recurrence. In the 2-dimensional case no integral symmetry lattice is claimed. Independent verification has not been performed.
