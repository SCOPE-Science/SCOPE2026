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
# Mathematical verification

Execute `python verify.py` with Python 3.10 or later (standard library only). It independently evaluates Legendre signs on every four-subset for the primes 5, 13, 17, 29, 37, and 41; checks all three predicted class counts, the basic quadratic-character sum for nonzero shifts, and exact integer characteristic polynomials of the signed four-by-four matrices. The observed result is `PALEY_FOUR_COLUMN_CHECKS_PASS 194317`.

This enumeration is finite and is not proof for all primes. The general proof is the switching reduction and exact character-sum identity in RESULT.md. Mathematical originality and independent validation have not been established externally.
