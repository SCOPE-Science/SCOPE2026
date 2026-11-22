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

# Verification notes

The standalone script `verify_mixed_dihedral.py` (Python standard library) tests all 243 additive endomorphisms of the group \(C_9\oplus C_3\) for idempotence, enumerates all 136 nontrivial generalized dihedral retractions, checks group multiplicativity and composition idempotence directly, computes their commuting pairs, and enumerates every maximal commuting family. Run `python verify_mixed_dihedral.py`; expected terminal marker `MIXED_DIHEDRAL_CHECKS_PASSED`. It separately verifies the one- through three-tuple closed formulas and a comparison case with cyclic exponent \(27\). This is finite corroboration; the complete proof is in RESULT.md. Historical priority and independent mathematical review have not been certified.
