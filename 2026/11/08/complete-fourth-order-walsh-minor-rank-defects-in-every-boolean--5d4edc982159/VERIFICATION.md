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

# Reproducibility checks

The complete theorem is derived from character-sign normalization and the affine classification of four distinct binary vectors. It is then reduced to an explicitly finite enumeration of projected triples of size \(4^3\) or \(8^3\), with lift weights given by falling factorials. This finite core is exactly evaluated as a cubic polynomial; it remains valid for every Boolean dimension, without inductive extrapolation from finite cases.

`verify_walsh.py` requires Python 3, standard library only. Invoke `python3 verify_walsh.py` in the directory containing it. The completed execution reported `ALL_FOURTH_WALSH_MINOR_CHECKS_OK`. Its checks include polynomial coefficient verification via six distinct lift values (more than the four required for equality of cubic polynomials), full column-subset ranks for both affine classes through dimension five, direct fourth-order real ranks and determinants for dimensions three and four, and the determinant-moment identity.

Limitations: finite recomputation corroborates the mathematical reduction and exact finite core; it is not an externally certified proof. No independent audit has been performed. Rank is over the real or complex numbers, and all counts are for the unnormalized Boolean Walsh matrix only.
