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

# Reproduction and limits

Execute `python verify.py` with Python 3 and SymPy. There are no data files, network dependencies or random seeds. All calculations use exact symbolic rational expressions. The verifier was executed successfully on the packaged source with the following output:

```
PASS: symbolic stationary expansion and linear/quadratic coefficients
PASS: all-parameter quartic onset on the nongeometric cancellation curve
PASS: exact nonsymmetric witness with nonzero fourth-order rectification
PASS: both symmetry conditions absent in the distinct-rate family
PASS: 18 independent matrix-tree and stationarity checks
ALL_CHECKS_PASSED
```

The verifier constructs the six states from two-element subsets of the four-site ring; builds the full biased generator and oriented bond-current row directly from the hopping rule; checks all column sums; checks the zero-bias distribution; solves the normalized stationary perturbation series; compares the exact quadratic and quartic coefficient rational identities; and independently calculates stationary probabilities by principal minors of the Markov generator on 18 rational parameter cases. Positivity and normalization are checked for those cases. The analytic proof of irreducibility and the exhaustive zero-locus classification use the full six-state model and positive denominator factorizations, not finite sampling.

The conclusions are specific to \(L=4\), \(N=2\), strictly positive rates \((a,b,1,1)\), and weak-bias Taylor coefficients. The verifier does not establish results for other ring sizes, other physical models, arbitrary precision numerical experiments, or independent proof review.
