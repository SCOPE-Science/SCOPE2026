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

Run `python3 checker.py` using Python 3 with only the standard library. The program enumerates all signed faces for ranks one through five and computes each oriented boundary's rank in characteristics two, three and five, comparing every degree with the closed binomial formula. It separately enumerates bounded signed integer exponent vectors, checks that the sign operation lies below the identity, and verifies monotonicity on every comparable pair. It prints `PASS: 132 exact finite homology and sign-retraction assertions`.

The structural proof uses the word-length-compatible order retraction, matroid shellability, exact Euler count, compatibility of consecutive inclusions and flag transitivity of signed permutations. The finite tests do not independently prove any infinite-range assertion or exclude torsion. No independent audit has been performed.
