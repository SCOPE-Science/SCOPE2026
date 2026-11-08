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

# Reproducibility and limits

Run `python3 checker.py` with standard Python 3. The program fixes the first of two linear orders and exhaustively varies the second for all domain sizes from three through seven. It prints `RANK_TWO_SUCCESSOR_EXHAUSTIVE_OK` only after exact moment and clean-signature checks pass. The checked sample space has 5,910 labelled relative permutations.

The full theorem is not a finite enumeration: its infinite proof is the forced-adjacency contraction identity, the mixed factorial-moment error comparison, the high-probability clean-frame reduction, and the rank-two logical normal form in RESULT.md. The program does not certify either the multivariate asymptotic for arbitrary numbers of orders or historical novelty. No independent validation has been performed.
