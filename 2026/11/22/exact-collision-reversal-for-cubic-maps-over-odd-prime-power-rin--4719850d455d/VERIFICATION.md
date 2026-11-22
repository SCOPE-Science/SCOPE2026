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

Run `python3 verify_cubic.py` with Python 3 and no external dependencies. The executable checks complete image-fiber histograms for 474 finite parameter combinations, direct ordered pairs for all tested moduli at most 100, and the exact critical-class difference for five primes at four exponents. The largest modulus in the exhaustive histogram suite is 6561.

The mathematical proof is algebraic, using a finite-field conic count, local transverse-coordinate bijections, and an exact valuation enumeration at each crossing. The finite tests do not certify the theorem for untested primes, parameters, or exponents. The odd-prime unit-coefficient domain excludes even moduli and coefficients divisible by the prime. Independent audit has not been performed.
