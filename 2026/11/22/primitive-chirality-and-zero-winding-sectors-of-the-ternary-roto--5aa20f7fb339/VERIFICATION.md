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

# Verification scope
The standard-library `check.py` independently constructs all cyclic loop-free words for lengths 2 through 12, detects least periods by direct divisibility, quotients by cyclic rotations, and checks exact formulas for total, zero-winding, and achiral primitive orbits. In particular it verifies the length-eight split (30,24,18). This is finite diagnostic evidence only; all-length statements follow from the combinatorial proof in `RESULT.md`.

The result makes no claim about actual realization by physical three-rotor trajectories. Review is same-model only; independent auditing remains unperformed.
