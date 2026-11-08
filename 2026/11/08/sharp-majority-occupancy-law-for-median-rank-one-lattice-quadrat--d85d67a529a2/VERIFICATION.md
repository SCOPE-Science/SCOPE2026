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

The exact algebraic root-of-unity reduction, orthogonality of cosine modes, sharp median variational argument, multinomial enumeration, strong-law limit, binomial large-deviation exponent and half-pool symmetry are proved in `RESULT.md`.

Run `python3 verify.py` with Python 3. The standard-library-only checker independently evaluates finite lattice averages, enumerates all small slope samples and majority-support subsets, compares rational exact distributions, and checks odd-binomial symmetry. The recorded run returned `PASS: 19584 independent finite assertions`.

Finite tests are not a proof for all primes or all repetition counts. The asymptotic rate uses Stirling's formula and the almost-sure limit uses the strong law of large numbers. No external or independent scientific validation has been performed.
