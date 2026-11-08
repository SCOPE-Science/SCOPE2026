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

# Verification notes

`VERIFY.py` uses only Python 3 standard-library exact rational arithmetic and exhaustive permutations of at most seven labels. Invoke `python3 VERIFY.py` in its directory; six configurations include two- and three-block rates and unequal as well as equal weights. Assertions compare every class-word conditional joint falling-factorial moment up to total degree three with the exact formula given in the proof. Additional numerical checks bound the explicit Poisson intensities in their expected interval and reproduce the uniform-rate mean of one.

The verifier terminates with a `PASS` line listing \(7{,}126\) comparisons and boundary checks. These finite checks support the combinatorial identity; they do not prove any infinite-sample convergence. For the latter, read the complete proof in `RESULT.md`: exponential-clock weak laws and rank quantiles prove eligible-slot convergence; bounded conditional factorial moments and a dominated generating-function expansion prove the joint Poisson law. The fixed-parameter positive-block hypotheses are essential. No independent audit has been performed.
