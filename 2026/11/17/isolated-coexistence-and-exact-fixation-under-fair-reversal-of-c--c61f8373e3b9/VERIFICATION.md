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

# Verification record

The included `check_cyclic.py` executed with Python's standard library and printed:

```
CYCLIC_VOLTERRA_EXACT_OK words=62 kernel=PASS Lyapunov=PASS martingale=PASS
```

For the rational cyclic coefficients \((a,b,c)=(1/2,1/3,1/4)\), this checks the fixed positive kernel, both sign maps fixing it, strict positivity, simplex preservation, pathwise weighted-product contraction on all sign words of length at most five, and exact conditional martingale and quadratic-variation identities. Only finite histories are enumerated. General almost-sure convergence, the stationary-law census, and all infinite-time extinction exponents follow from the analytic proof in `RESULT.md`, not from this finite checker.

No independent external mathematical audit is claimed or recorded.
