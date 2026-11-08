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

# Reproduction and limitations

The proof is self-contained in `RESULT.md`. The Python standard-library checker is `checks/check_periodic_projection.py`. From the package root, run:

```sh
python3 checks/check_periodic_projection.py
```

The checker uses exact `fractions.Fraction` Gauss–Jordan inversion of the cyclic hat-function Gram matrices for each \(n\) from \(3\) through \(21\); computes each knot evaluation kernel's \(L^1\) integral by exact rational formulas; compares those values with the explicit periodization expression using high-precision `decimal.Decimal`; and independently integrates the parity-overlap functions against the two convergent series formulas. The observed output is:

```text
EXACT_RATIONAL_GRAM_INVERSE_AND_INTEGRAL_OK 19
PERIODIC_PARITY_ASYMPTOTIC_CONSISTENCY_OK
INDEPENDENT_OVERLAP_INTEGRATION_OK
LEADING_COEFFICIENTS 1.6830464193182701 0.7011506234329134
ALL_PERIODIC_LINEAR_SPLINE_CHECKS_OK
```

The proof that these coefficients control the infinite subsequences requires the geometric decay of the discarded translates and the explicit decomposition of the piecewise-linear overlap integrals; finite numerical or exact-rational checks do not establish that limit. The decimal approximations represent convergent-series coefficients and are not the formal definitions of the constants. No independent mathematical audit has been performed.
