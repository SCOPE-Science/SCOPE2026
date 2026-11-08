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

Run `python3 verify.py` using Python 3 and only its standard library. The observed output was:

```
VERIFY_OK
Direct independent KMP words: 121485 (every binary word with two ones, lengths 2..90)
Bivariate rational-series coefficients: all degrees <=35, all possible borders
Exact count normalization and sharp maximum: lengths 101,202,500,1000,2000
Rational moment identities: mean 7/27, second moment 5/54, variance 37/1458
Uniform local-limit count discrepancy at selected large lengths: <=6
```

The KMP prefix function calculates border lengths by a method independent of the zero-gap classification. The rational-series expansion uses multivariate formal power-series arithmetic. Selected large sizes verify count normalization, the sharp maximum, and an explicit constant discrepancy from the predicted local limit. Exact rational arithmetic checks the limiting moments. These finite checks cannot prove the asserted formulas for arbitrary length; the general proof is in `RESULT.md`. Independent mathematical audit has not been performed.
