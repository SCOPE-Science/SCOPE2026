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

Run `python3 verify.py` from the same directory as the six prose/data files. Only the Python standard library is required. The program derives complete-graph cycle and Frobenius matrices independently, proves by exact integer determinants that the proposed bases are unimodular for each checked value \(4\le n\le11\), checks every Frobenius matrix in that basis, and independently counts normalization components, singular nodes and branches over sample extension degrees. The recorded successful output in `CHECKS.txt` ends with `CYCLIC_GENERIC_LINE_PICARD_INTEGRAL_LATTICES_AND_ZETA_OK`.

The finite test is not an infinite proof. The unrestricted theorem rests on the algebraic general proof in `RESULT.md`, including primitive chord elimination, the antipodal cyclic module, Frobenius coinvariants, and normalization. No independent audit has been performed.
