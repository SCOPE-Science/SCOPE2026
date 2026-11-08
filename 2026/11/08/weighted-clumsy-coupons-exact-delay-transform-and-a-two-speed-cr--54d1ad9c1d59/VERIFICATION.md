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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 and its standard library. On the supplied file, the deterministic output is:

```
PASS: 1168 deterministic exact/rational/numerical checks
two-class mean delay=2.329643650265; uniform benchmark=2.093519562628
Laplace at s=1/2=0.559753585943
```

The code checks finite stochastic-transition normalization and reversible product measures using `fractions.Fraction`, exact comparisons between a subset-sum stationary return transform and brute-force labeled Markov transitions, exact delay means/PGFs against independently solved absorbing systems, and finite majorization examples. It also compares a two-class limiting series with an integral, compares equivalent Laplace-transform expressions, and tests Poissonized cover probabilities at increasing finite sizes. The exact-rational checks verify specified finite inputs, not every positive weight vector; the floating checks are numerical consistency tests, not certified interval enclosures.

The proof of general finite identities, majorization monotonicity, and asymptotic laws is mathematical and appears in `RESULT.md`. In particular, empirical tests alone do not certify the weak limit, infinite-series exchanges, Schur convexity for arbitrary dimension, or historical priority. Independent validation has not been performed.
