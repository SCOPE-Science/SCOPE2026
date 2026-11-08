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
# Verification of the period-tail formulas

The proof in `RESULT.md` is self-contained and covers every real parameter in its stated domain. `CHECK.py` is an independent finite reproducibility check, **not** a proof of uniformity in the parameter or of any infinite limit. Python 3 with `sympy` and `scipy` is required to run `python CHECK.py`.

The checker verifies exactly (symbolically) that the cubic vector field is angular and that its reduced speed has the stated completed-square form. It numerically integrates the actual Euclidean-area density on an example torus with \(a=3/2\); evaluates the exact sublevel areas using the polynomial roots; and compares their \(\sqrt t\)-normalized values at \(t=10^4\) and \(t=10^6\) to the analytical scaling profile for five fixed \(\lambda\) values.

Representative independently executed output:

```
EXACT_POLYNOMIAL_FLOW_AND_SQUARE_COMPLETION_OK
lambda -10 t 10000 scaled_tail 0.0 limit 0.0
lambda -2 t 1000000 scaled_tail 0.528324092 limit 0.528322901
lambda 0 t 1000000 scaled_tail 0.631836158 limit 0.631834827
lambda 2 t 1000000 scaled_tail 0.720629908 limit 0.720628482
lambda 10 t 1000000 scaled_tail 0.551242734 limit 0.551240152
CROSSOVER_FINITE_CHECK_OK
```

The subcritical mean-coefficient calculation was additionally evaluated at \(a=3/2\) for gaps \(10^{-2},10^{-3},10^{-4}\); the rescaled means respectively approached \(2.7929691,2.6360427,2.5837398\), consistent with the analytically proved limit \(2.5591061\). This extra diagnostic is not embedded as a separate code dependency. Endpoint singularities in the area density are integrable; all tail constants use interior points. The moment thresholds follow from a standard one-dimensional local integral, not finite enumeration.

Independent mathematical audit: not performed.
