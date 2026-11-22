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

The proof is in `RESULT.md`; `check.py` is a standalone Python 3 standard-library supplementary calculator. Run from the folder containing the two files:

```
python3 check.py
```

The actual extracted checker execution returned `PASS: 19007 independent numerical/algebraic assertions`. Its randomized parameter tests inspect derivative signs, monotonicity of the threshold function, strict uniqueness regimes, equality of endpoint shares and selected asymptotic behavior. Those finite checks are not exhaustive and do not establish correctness for arbitrary real parameters; the proof establishes the universal quantified theorem via an increasing conditional tail average.

Analytic normalization uses \(q=e^{-\lambda_1t}\in(0,1)\) and \(S_v(q)=(1-q^v)/(1-q)\); the boundary \(t=0\) is not an observed positive-depth sequence library. Proof arguments handle the endpoint equalities and the strict positive-time inequalities separately. The model applies only to independent positive saturations and a conditional fixed-depth sequencing sample; no empirical parameter estimates or independent external validation are asserted.
