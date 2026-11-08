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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no external packages. The checker evaluates the exact aggregate count-process recursion against an independently written recursion over labelled available vertex subsets for three small graph sizes and four weak-edge weights (including zero), with exact `fractions.Fraction` arithmetic; it verifies normalization, nonnegativity, the analytic mean bound for five additional sizes, and seeded Monte Carlo smoke checks in three weak-rate scaling regimes.

Observed program output:

```
PASS 52 exact-rational identities and seeded statistical smoke checks
Limitation: finite-state checks and simulations do not prove the asymptotic theorem.
```

The claimed asymptotic distribution and moment convergence follow from the proof in `RESULT.md`; no finite computation or simulation is used as an infinite theorem. Independent external audit has not been performed.
