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

# Verification and reproducibility

The included `verify.py` can be run with Python 3 without third-party modules:

```sh
python verify.py
```

The verifier enumerates crossed simplex face subsets in small dimensions, independently compares Gaussian pairwise correlations, performs Monte Carlo normalization checks for the exact finite-dimensional mean, and couples high-dimensional Gaussian sign vectors to the macroscopic limit. It also checks the simple moment identities at the displacement endpoint and the crossover variance expression. All comparisons use the exact source file packaged with the result.

**Scope of evidence.** The infinite-dimensional results are analytic statements proved in the accompanying `RESULT.md`: the local empirical-CDF fluctuation bound, the central limit theorem, the strong/uniform empirical-CDF convergence, and polynomial face-count expansion establish them. Neither the Monte Carlo log nor finitely many enumerations certify an infinite limit or exhaust all parameters. The historical-literature comparison has explicit remaining priority risk. Independent audit has not been performed.
