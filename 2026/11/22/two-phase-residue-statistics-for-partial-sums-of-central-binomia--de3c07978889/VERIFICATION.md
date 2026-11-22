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

## Reproducibility

Run `python3 verify.py` using the standard library. The checker reconstructs the matrices from the five stated digit rules, checks the twenty exact integer rational-certificate equations without floating point, and verifies the two rational limiting distributions.

It then compares 201 explicit integer binomial coefficients with their base-five Lucas products, verifies the recurrence for all indices below \(5^4\), and enumerates all residues of running partial sums over cutoffs \(5^r\) for \(1\le r\le7\). Each computed vector is checked against stored integers and the proven error bound.

Observed output:

```
PASS: 20 exact matrix equations; 5 rational limiting frequencies;
      201 direct binomial congruences; 7 complete block histograms;
      transition checks and rigorous finite-depth error bounds.
even: 1/14, 4/7, 1/7, 1/14, 1/7
odd:  1/14, 1/7, 1/14, 1/7, 4/7
```

The infinite result is proved by the exact digit recurrence and almost-sure first-absorption coupling. Finite tests alone would not certify the limiting law. Independent mathematical audit has not been performed.
