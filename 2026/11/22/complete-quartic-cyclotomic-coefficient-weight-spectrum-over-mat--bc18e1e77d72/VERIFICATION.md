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

# Verification of the exact finite coefficient-weight spectrum

Run `python3 verify.py` with Python 3 and the standard library only. The checker traverses every one of the 3584 monic quartics with nonzero constant term over the field defined by the binary polynomial `0b1011`. It tests irreducibility against `X**64-X`, counts exact coefficient weights, and determines root orders through modular exponentiation.

Independently it represents the degree-four extension as `F8[z]/(z**4+(u+1)*z+1)` and verifies an explicit primitive element of multiplicative order 4095. Every exponent orbit under Frobenius multiplication by eight is inspected and its minimum polynomial multiplied out from its four roots; these independent counts are compared with all eighteen expected rows.

The script also checks the modular order 585 of the base trinomial `X**4+(u+1)*X+1`, total 1008 monic irreducible quartics, and total 56 trinomial quartics. On replay it printed `PASS: two independent full quartic enumerations; 1008 factors in 18 orders` with the exact counts in `RESULT.md`.

The finite enumeration is exhaustive for the stated field and degree. It does not imply results for other finite fields or higher degrees; no external independent audit is claimed.
