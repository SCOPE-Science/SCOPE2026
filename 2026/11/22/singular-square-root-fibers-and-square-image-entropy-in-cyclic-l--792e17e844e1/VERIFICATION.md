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

The exact finite-field checker `check_roots.py` enumerates each prescribed square-root fiber of the radical edge-product map for fourteen parameter pairs, including a non-prime field order, and separately computes the image size using the four-state matrix. The recorded output `check_roots_output.txt` reports all checks passing. For each pair, all prescribed targets are tested, not just samples. These are finite sanity checks and do not establish the general theorem.

The general result is proved by path-basis reduction, independent-set factorization on zero gaps, a cyclic multiplicative consistency equation for all-nonzero targets, and a primitive transfer matrix for the image law. The root-counting theorem applies for every prime power and every cycle length at least three; the entropy statement holds at fixed field size as the cycle length grows.

Historical originality is a reasoned literature comparison, not a formal priority certificate. No independent audit has been performed.
