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

# Verification of the two-site OU energy theorem

Run `python verify.py` in this directory after installing packages in `requirements.txt`. This checks exact rational/algebraic matrix reductions with SymPy; symbolic centered-eigenvalue, collision-derivative and endpoint-derivative identities; and the first seven nonzero coefficients of the analytic hyperbolic power-series certificate. The infinite-tail coefficient positivity is proved for every integer index in `RESULT.md`, not inferred from the tested coefficients.

Numerical tests performed: 7,958 direct matrix-trace comparisons of centered and shifted pairs at equal gaps over eight dimensionless horizons; eight finite-horizon optimization comparisons including exact matrix evaluation; and high-precision computation of the unique long-horizon gap and gain, with three large-horizon convergence checks. Random finite tests are supplementary only and do not establish universal optimality. The actual output was:

```
PASS symbolic matrix identity, centered spectrum, endpoint derivatives, positive-series coefficients
PASS 7958 independent centered-vs-unrestricted placements and finite-horizon checks
Asymptotic gap: 2.554928950095267006479 limiting score: 2.018185556085661528264
```

The core nonstandard assertions are checked by the written proof: strict centering from AM–GM and monotonicity in the margin sum; strict interiority from signed endpoint derivatives; uniqueness of the limiting gap from positivity of all power-series coefficients and strictly concave log excess; convergence of arbitrary optimal gaps by excluding zero and escaping infinity. The theorem does not claim finite-horizon gap uniqueness or independent validation.
