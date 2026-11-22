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

The standalone `verification/check.py` reconstructs all twelve seed certificates and checks every member of every progression by exact integer arithmetic, in addition to a sieve certificate excluding prime factors through the necessary digit-sum bound. It prints `VERIFY_OK bases=12 terms=1594356`. The proof in `RESULT.md` independently establishes the universal parity bound and the modular-order construction of infinitely many starts. Unlisted exponents remain unproved. There has been no independent scientific audit.
