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

Run `python verify.py` from this directory using the Python standard library. The script independently calculates the rational-point count of \(Y^2=X^3+13X^2+128X\), the collision count and the histogram for both choices of unit, and compares them to the theorem. It enumerates all odd prime fields of size at most 97, excluding 7, and the five quadratic extensions of size 9, 25, 121, 169 and 289, for 28 finite fields total.

Expected first output line: `ELLIPTIC_CUBIC_OK 28 finite fields`. The calculation tests finite instances only; the discriminant, point-count and incidence proofs in RESULT.md establish the claimed infinite field range. The 2- and 3-torsion arguments and the smoothness exclusions are explicit in the proof. Independent audit has not been performed.
