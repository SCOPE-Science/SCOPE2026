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

The complete algebraic/topological proof is in `RESULT.md`. Run `python3 verify_wheel.py` from this directory using Python 3.9 or later; no third-party modules are required. The program tested 42 rotation patterns for wheel rim orders 3 through 9, including every orbit-subset for each, and the fixed-spoke cone criterion for five odd rim orders. It also independently computed small fixed-space reduced Euler characteristics. The exact returned marker was `WHEEL_FOREST_ROTATION_FIXED_LOCI_AND_ODD_DIHEDRAL_CHARACTER_OK 42 5`.

Finite checks do not prove the statements for unbounded rim orders. The general proof depends on the explicit rim-covering criterion, the standard shellability theorem for matroid independence complexes, and the elementary chromatic-polynomial calculation. Only the cyclic rotation fixed-space result is claimed as new; the nonequivariant wheel homology count and related representations were previously known.
