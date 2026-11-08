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

# Verification of the least-period theorem

Use `python3 verify.py` with standard-library Python 3. The script reproduces all branch parameters for moduli 2 to 60, checks that no proper-divisor branch equals the residue-zero branch, and independently enumerates excluded quotient-semigroup elements for a finite set of `(p,a)` to compare exact Frobenius numbers against the published branch formula. It uses only exact integer arithmetic. The unrestricted theorem follows from the proof in `RESULT.md`, including the divisor-orbit witness and CRT argument, not from any finite computation.

No external audit or certification has been performed.
