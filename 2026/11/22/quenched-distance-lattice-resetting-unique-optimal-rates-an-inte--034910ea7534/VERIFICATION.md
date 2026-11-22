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

The conditional mean was independently checked against a finite-volume backward generator boundary-value computation for sites 1 through 8 and positive reset rates 0.25, 0.8, 1.7, 4, and 12. A standard-library Python script (`checker.py`) tests multiple finite mixture laws, sign changes of the exact derivative polynomial, and the rare-distance scaling across different maximal distances and contamination probabilities. Reproduce with `python checker.py`.

The full infinite-support classification follows from Tonelli's theorem, the radius of convergence of the positive tail series, and strict positivity of \(N'(y)\). The boundary example follows from an explicit absolutely convergent rational inequality. None of these infinite-dimensional assertions is inferred from truncated numerical tests. A human-independent scientific audit has not been performed.
