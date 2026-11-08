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

# Reproduction and limits
Run `python3 check.py` using a standard Python 3 interpreter. The source explicitly generates all exterior basis subsets as bitmasks, multiplies general elements, and checks the wedge-map reduction by literal multiplication. Its finite-field tests enumerate \(3^{10}\) degree-one input pairs for selected targets, compute ranks of actual coefficient matrices, and compare fiber populations with the proposed formulas. The complete sample output is in `check_output.txt` and ends in `ALL_FIFTH_EXTERIOR_COMMUTATOR_CHECKS_PASS`.

These checks provide finite corroboration, not proof for arbitrary \(q\). The proof in `RESULT.md` gives the unrestricted statements. No independent audit has yet been performed.
