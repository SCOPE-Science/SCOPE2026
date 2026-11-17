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

The proof is entirely analytical and covers every real bi-infinite discrete-BV sequence. The supplied `verify_cardinal_cubic.py` uses exact symbolic arithmetic to confirm the integer-knot second-derivative recurrence, geometric decay, tail turning point, primitive and radical constant. It independently assembles the finite-band cubic natural spline equations, integrates signed derivative cubics cellwise between real roots, verifies the step constant and stresses the all-input upper bound on 1,200 random jump sequences. The finite system is only a numerical corroboration of the infinite theorem; sharpness and all-input validity follow from the exact proof, not a finite matrix or statistical search.

Run `python verify_cardinal_cubic.py`. Expected terminal markers:

```
EXACT_GREEN_RECURRENCE_AND_ALL_ORDER_STEP_TAILS_PASS
INDEPENDENT_FINITE_MATRIX_AND_RANDOM_BV_STRESS_PASS 1200
ALL_CARDINAL_CUBIC_VARIATION_CHECKS_PASS
```

For reproducibility, packages required are Python, `sympy`, `numpy`, `scipy`. The historical Schoenberg chapter was not available in full; no independent mathematical audit has been performed.
