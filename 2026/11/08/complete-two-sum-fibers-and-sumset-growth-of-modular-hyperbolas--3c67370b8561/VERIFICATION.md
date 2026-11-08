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

The complete proof is in `RESULT.md`; the executable `CHECK.py` is a separate corroborative verification, not the source of the unrestricted theorem.

Execute `python CHECK.py` from the directory containing this file. It exhaustively forms all ordered two-sums of modular-hyperbola points, computes the predicted representation number for each possible target using integer square-root counts, and independently checks both the sumset size and ordered additive energy. The prime-power cases include \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(7,3),(11,1),(11,2),(13,1)\). Nine additional composite cases check the Chinese-remainder product law.

The saved-package replay passed with the line `CHECK_OK moduli=22 target_slots=231934 all_multiplicities_exact=True`. No floating-point root detection, randomness, external datasets, or third-party Python packages are used. Finite enumeration establishes only the tested cases; all prime powers and odd composite moduli are justified by the written proof.

The fourth-moment formula is verified analytically through additive-character orthogonality. The earlier field case and some one-variable Kloosterman moment implications are prior knowledge, not evidence of novelty. Independent audit has not been performed.
