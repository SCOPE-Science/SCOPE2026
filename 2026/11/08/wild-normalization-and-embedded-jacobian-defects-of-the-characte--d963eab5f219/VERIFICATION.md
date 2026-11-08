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

The attached script `verify_steiner.py` performs exhaustive exact-field checks for degrees \(1,2,3,4\) over \(\mathbb F_2\). It iterates projective coordinates, evaluates the quartic, evaluates all derivatives, enumerates the normalization map, and checks the predicted rational-point and singular-locus formulas. The recorded output is `verification_output.txt`. The checks are finite tests; the universal claim follows instead from the proofs in `RESULT.md`.

Critical independent human checks remaining: historical comparison against inaccessible complete 2012 Steiner paper, and expert review of the general characteristic-two normalization and conductor argument.
