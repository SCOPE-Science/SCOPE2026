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

# Reproducible verification

Run `python3 verify_density.py` with Python 3 and no third-party libraries. It exhaustively loops over all \(26,732,160\) ten-prime exponent vectors, computes the local comparison ratios from actual divisor sets of exponents, sums only weights satisfying an exact cross-product inequality, and asserts the precisely stated integers \(N,Q\) and \(397N>308Q\). A second exact-rational calculation enumerates the primes between \(31\) and \(997\) by trial division and verifies the finite part of the tail estimate. The remainder is proved by the analytic integral in RESULT.md rather than by a cutoff test.

Observed replay result:

`VERIFY_OK vectors= 26732160 prime_tail_check= 158 N= 22146947537280283084803283684585457657160649113600 Q= 28535726520270636024768604478765044285962240000000`

`certified_lower= 0.7702921253866226 finite_prime_sum= 0.007109822774371849 strictly_greater_than_77_percent=PASS`

Floating-point numbers above are display-only. All decisive assertions are exact integer or rational arithmetic. The certificate does not calculate the true density or settle the equality-case infinitude question. No independent mathematical audit has been performed.
