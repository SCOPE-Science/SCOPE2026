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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script obtains the signed-digit correction both from consecutive values of \(B(n;k)\) and by explicit enumeration of the six leading-prefix classes, then compares these with the separate bounded-digit Fibonacci generating-product dynamic program. It checks the sixteen initial values reported in the motivating paper, finite cases of the effective stabilization bound, and the combinatorial summatory bounds. All arithmetic is integral, without floating point or randomized evidence.

The proof of the unrestricted product and summatory exponent is in `RESULT.md`. Exhaustive finite checks are limited to the program's displayed finite ranges and do not prove anything about larger, unexamined indices. The verification record contains no assertion of independent mathematical certification.
