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

# Reproducible mathematical verification

Run `python3 checker.py` using the package's included Python 3 standard-library checker. The checker directly computes hitting-time expectations on finite absorbing Markov states for every pair of sizes 1 through 7 and five rational choices of class-source probabilities. It also reconstructs deadline distribution functions by exact finite-state probability propagation and checks them against the binomial-strip formula at five deadlines. The recorded run produced:

```
PASS exact mean and all deadline CDF checks: 1470
```

The mathematical proof in `RESULT.md` establishes all finite-size identities and the asymptotic normal-quantile optimization. The finite program does not certify a limit theorem or prove literature priority. Independent audit: not performed.
