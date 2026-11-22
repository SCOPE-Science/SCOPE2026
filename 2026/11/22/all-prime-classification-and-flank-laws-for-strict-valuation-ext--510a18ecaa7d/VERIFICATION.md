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

The proof is mathematical and self-contained, using an exact rational quotient, valuations of products, congruence elimination, and exact affine root frequencies. Execute `python3 verify.py` with Python 3 standard library to independently reconstruct valuations from factorial valuations. The checker reports `PASS: 2160972 exact assertions over 18 primes, n < 20000` on the supplied source. It tests the exact jump, all peak and valley classes, all exact flanks, and small-index direct binomial values.

Finite exhaustive tests over the stated index ranges do not prove unrestricted claims; those follow from the explicit prime classification and residue arguments in RESULT.md. No external proof-assistant, third-party certification, or independent audit has been performed.
