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

The exact period-closing lemma is proved by repetition for proper borders and by shortest return-path completion for border-free words. Perron–Frobenius powers establish the fixed-border probabilities and product boundary distribution. A geometric union bound controls large borders uniformly; truncation plus mixing proves exponential total-variation and moment convergence.

Run `python3 check.py` to repeat finite exhaustive comparisons between the exact formula and independent enumerations of periodic completions, and to inspect the sample border moments on two small primitive matrices. These finite checks do not replace the proof of the infinite claims. The numerator in the directed lower bound excludes one explicitly counted border event before applying the union bound. Independent mathematical validation was not performed.
