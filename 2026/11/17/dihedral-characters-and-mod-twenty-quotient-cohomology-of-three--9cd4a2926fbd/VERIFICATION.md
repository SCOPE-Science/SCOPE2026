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

# Verification and limits

Run `python3 verify_character.py` with the standard Python library. The expected complete stdout is included in `verification_output.txt`; the verifier fails on any discrepancy. It checks the integer matrix equation \(T^5=-I\), the independently constructed reflection-string recurrence, and the averaged character for each length between 12 and 150. It also enumerates every admissible face and independently computes signed permutation traces of all dihedral elements at lengths 12 through 17 (174 elements). This is a finite consistency check, not a certification of the universal proof, which is given in RESULT.md. The cited prior theorems supply the single-degree homology concentration.
