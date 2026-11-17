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

# Computational verification
Run `python3 VERIFY.py`. The script uses exact integer boundary maps and checks the full eight-element dihedral action, the two spoke-pair obstruction, the explicit 29-term signed cycle, and its rim coefficient \(-2\). The expected output is stored in `VERIFY_OUTPUT.txt`. The parity proof itself is a universal chain-coefficient argument for this finite complex, not a statistical inference from enumeration. No homotopy classification beyond the standard shellability of independence complexes of matroids is claimed; no independent mathematical certification is implied.
