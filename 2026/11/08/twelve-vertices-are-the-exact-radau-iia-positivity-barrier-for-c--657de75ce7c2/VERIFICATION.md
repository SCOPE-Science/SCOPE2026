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

# Verification

Run `python3 verify.py` with the standard Python library. The script constructs exact Laplacians for 31 multipartite profiles, forms the full Radau rational transition by exact matrix inversion, independently evaluates the explicit entry formulas, checks stochasticity and nonnegativity for orders at most eleven, and verifies the diagonal witness in each tested part for orders at least twelve. It also checks 741 witness expressions for all integer pairs \(12\le N\le50\), \(1\le p<N\). The package-extracted replay produced:

```
PASS 196 exact matrix/witness cases, 16580 exact entries, 1510 row sums;
PASS witness expression negative for 741 integer pairs of orders 12..50;
NOTE finite tests are not a proof for unbounded graph order or all timesteps.
```

The universal statements are proved by spectral-projector identities, an explicit global minimum of the stability function, and a universally positive polynomial inequality in `RESULT.md`. Finite tests are supplementary and do not prove global optimality or exhaustive graph coverage. Source comparisons were mathematical and do not imply independent publication-priority verification. No external or independent audit has been carried out.
