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

Run `python3 verify_picard.py` and `python3 verify_arithmetic_chambers.py`, then `python3 verify_all_permutations.py` from the extracted package. The first program verifies the integral geometric pairings. The second program independently enumerates supports and Galois-orbit unions and checks all eleven arithmetic types, the two-count distinction, and the known geometric total. The third uses the independent star/triangle family method and verifies all 720 permutations. The `chamber_table.json` file gives full size-by-size counts for reproducibility. The geometric exhaustiveness step is the proved negative-curve classification and negative-definiteness criterion in `RESULT.md`; the finite program is not evidence for an unproved infinite claim. No independent audit has been performed.
