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

# Verification

Run `python verify_associators.py` with Python 3 standard library only. The script independently generates symmetric and dihedral multiplication tables, calculates the inverse-property loop multiplication, enumerates each ordered associator triple, independently counts all group commutators, and checks the complete elementwise fiber equality. Its finite cases are \(S_3\), \(S_4\), \(D_8\), and \(D_{10}\). The asserted all-groups formula depends on the eight-case symbolic reduction in `RESULT.md`, not on finite tests. The script also verifies the odd-dihedral closed form at orders six and ten. No independent mathematical audit has been performed.
