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

# Exact supplementary verification

Run `python3 verify.py` with Python 3 and its standard library. The script independently evaluates the alternating divisor sum from prime-power factors for exponents \(1\le a\le24\), confirms the remaining large solution with exponent \(31\), tests the local Fermat-power lemma for odd primes less than 150 and exponents through 15 (510 cases), and checks exact small Fermat numbers and the compositeness witness \(4294967297=641\cdot6700417\).

The expected output is `VERIFY_OK direct_exponents=1..24 solutions=[1, 2, 3, 7, 15] extra_exponent=31 PASS local_odd_prime_power_tests=510 Fermat_primality_F0..F4=PASS F5_composite=PASS`.

The script is a consistency check, not a proof for unbounded exponents. The unrestricted result follows from the elementary prime-power factorization and multiplicative-order argument given in RESULT.md. Independent audit: not performed.
