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

The exact-rational, finite-size checker can be run using `python checker.py` (Python 3 standard library only); it completed 17,939 assertions without an exception. It enumerates finite words, evaluates their probabilities exactly, and tests both graph orientations, the deletion inequality and the variance bound. The proof of the infinite-alphabet theorem is in `RESULT.md`; the finite checker does not certify infinite-dimensional limits, analytic Poisson approximation, or historical originality.

Separate numerical diagnostics used NumPy's Zipf sampler with exponent 2 and 18 samples per sample size (10,000, 50,000, 100,000) at a fixed pseudorandom seed; the observed directed means were 566.2, 1444.5, 2174.2, versus second-order predictions 565.0, 1457.3, 2179.0. These diagnostics are supplementary, and the core package requires no numerical external dependencies.

Self-review passed for the stated theorem. Independent mathematical validation and external audit have not been performed. The primary remaining scientific risk is priority against more general but not identified infinite-alphabet pattern-count results.
