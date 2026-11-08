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

# Verification of the six-letter cutoff

Execute `python3 artifacts/verify.py`. The deterministic output is embedded as `artifacts/verify_output.txt`. The exact prime sieve checks all primes in the finite gap below the analytic threshold. The bit-window method is exhaustive, not sampled. A direct Euler-criterion implementation cross-checks 63 primes, including the boundary pair. At the prime 457 the missing mask is 63; at 461 all masks are present. The infinite range is proved separately in RESULT.md using the standard separable-polynomial Weil bound.

No independent external scientific audit has been performed.
