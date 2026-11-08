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

# Reproducible verification

Run `python check_muntz.py` with Python 3; only its standard library is required. The checker computes second and fourth moments independently by exact binomial expansion, rather than copying the optimized quadratic as a black-box numerical test. It compares all opposite-parity pairs in the displayed finite parameter grid against their rational optimum and extremizer ratios, and tests a local strict improvement for same-parity pairs. The recorded execution produced:

```
EXACT_PARITY_AND_MIXTURE_CLASSIFICATION_PASSED 2936 opposite-parity pairs
EXACT_SAME_PARITY_LOCAL_OBSTRUCTION_PASSED
ALL_MUNTZ_TWO_POWER_CHECKS_PASSED
```

## Analytical coverage

The mathematical proof treats **every** integer \(0\le\ell<h\). The exact phase check rests on the factorization of \(C-B\) and the signs of its quadratic numerator at \(5\ell+2\) and \(5\ell+3\), not on the finite enumeration. The sharp maximization uses exact completion of the square and an endpoint factorization. Same-parity nonattainment by pure monomials follows from an explicit nonzero analytic first derivative. The large-degree limit follows from the moment expressions. Neither finite verification nor available literature searches constitute an independent audit, and none is claimed.
