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

# Exact verification

Run `python3 verify_prime_power_triples.py` with Python 3 (standard library only). The script computes exact signed Fourier determinant exponents reduced by the prime-power cyclotomic polynomial, checks all two-by-two minors, and separately tests valuation formulas and full rank partitions. Exhaustive normalized index-triple tests cover prime-power orders 4, 8, 16, 32, 9, 27, 25, and 7. Additional formula-only partitions are evaluated at 81, 125, 343, and 14641. The expected success marker is `PRIME_POWER_TRIPLE_FOURIER_EXACT_CHECKS_PASS`. The tests do not exhaust infinitely many orders, which are instead handled by the proof in RESULT.md. An independent audit is not performed.
