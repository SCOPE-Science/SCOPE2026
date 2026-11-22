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

# Reproducibility and proof limits

Run `python code/verify_semigeneric.py` from the directory containing this document. The script enumerates exact parity-compatible diagrams over small fixed named bases, verifies the first several all-arity counts and changed old-base edge patterns, then checks exact arithmetic formulas and families in much larger finite ranges. The stored expected output is `verification/check_output.txt`.

The main proof does not extrapolate from these calculations. Its universal components are the surjective restriction of each row/column affine orientation space, the Stirling partition-sum count, the strict integer inequality separating equal-unary spectra with different class numbers, and the explicit collision-family identity. The checker is finite corroboration of these deductive claims.

No infinite mechanical proof certificate or independent validation is claimed. Historical publication priority is not certified by unsuccessful searches.
