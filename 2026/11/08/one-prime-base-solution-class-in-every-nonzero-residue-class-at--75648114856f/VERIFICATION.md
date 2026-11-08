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

Run `python3 verify.py` with Python 3. It evaluates each binomial product via exact integer modular inverses, tests unique lifts for prime-power moduli, and compares directly against integer binomial coefficients in a bounded range. The verified theorem for all primes and exponents comes from the displayed product congruence and lifting, not from finite enumeration. The density conclusion uses the classical prime number theorem for arithmetic progressions; it was not tested numerically. No independent audit has been performed.
