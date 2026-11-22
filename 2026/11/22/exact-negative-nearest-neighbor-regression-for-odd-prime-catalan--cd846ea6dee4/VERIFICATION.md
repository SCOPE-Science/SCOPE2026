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

# Reproducible checks

Execute `python3 verify.py` from a directory containing this file and the supplied standalone verifier. The verifier uses the Legendre factorial valuation formula for the two consecutive Catalan numbers and independently evaluates the ordinary Catalan integer values for 505 small cases, avoiding the carry expectations used in the proof. It tests 33 prime-depth combinations, covering 108,479 index pairs, complete drift histograms, and exact rational covariances.

Observed result:

```text
VERIFY_OK prime_depth_cases=33 exact_integer_indices=108479 actual_bigint_pairs=505 jump_histograms=PASS rational_covariance=PASS
```

The tests are finite consistency checks. The infinite conclusions depend on the written proof, particularly the complete classification of the two valuation root cylinders and the carry Markov expectation. Independent mathematical audit has not been performed.
