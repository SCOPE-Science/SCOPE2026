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

# Reproducibility and mathematical verification

Run with Python 3.8 or later: `python3 artifacts/verify.py`. The program uses only the Python standard library and tests exact cyclotomic-zero histograms, never floating-point thresholds. It prints `FOUR_ATOM_PARABOLA_CHECKS_PASS 104626` on success.

The implementation independently enumerates every four-point support for primes \(5,7,11,13\). It verifies the zero, two and complete-line witnesses by exact integer cyclotomic coefficients, and verifies the one-zero witness via two independent modular character equations. It additionally checks every phase choice in the coefficient alphabet \(\{\pm\omega^j:0\le j<p\}\) up to global scalar for every four-site support in primes \(5,7\). These calculations do not cover all continuous coefficient phases or all primes; the analytic proof in `RESULT.md` covers those quantifiers.

There is no independent or external validation in this package. The closest full-text priority risk is the unavailable complete 2026 finite-parabola preprint. The proof does not use inaccessible source assertions.
