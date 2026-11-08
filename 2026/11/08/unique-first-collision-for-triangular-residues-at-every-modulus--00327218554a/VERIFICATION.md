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

Execute `python3 verify.py` with standard-library Python 3 from the directory containing this file. The verifier directly enumerates the first repeated triangular residue for every modulus from 1 to 9999, compares the formula, checks uniqueness of the earlier witness, and tests the **integer** difference exactly equal to the modulus. Small prime-power closed forms are also checked.

The critical unlimited assertions are proved in `RESULT.md`: valuation splitting of the opposite-parity factors, attainment by a complementary factor pair, and strict uniqueness of the odd minimizing divisor. A bounded direct enumeration does not certify unbounded quantifiers; the code is a supplementary exact regression check.

No independent mathematical audit has been performed.
