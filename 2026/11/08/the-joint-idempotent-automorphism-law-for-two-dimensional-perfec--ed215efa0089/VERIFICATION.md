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

The exact algebraic proof is given in `RESULT.md`. The standalone `CHECK.py` computes finite fields by explicit polynomial arithmetic, enumerates all invertible \(2\times2\) structure matrices in nine fields, directly counts every rational nonzero idempotent and every field-rational monomial automorphism, and compares the full joint distribution to the theorem. The log in `CHECK_OUTPUT.txt` records `VERIFY_OK`.

The finite checks cover \(q=2,3,4,5,7,8,9,11,13\), including nonprime extension fields and both characteristics. They do not exhaust infinitely many fields, do not determine scheme-theoretic automorphism length, and are not substituted for the proof. This self-review is not an independent mathematical audit.
