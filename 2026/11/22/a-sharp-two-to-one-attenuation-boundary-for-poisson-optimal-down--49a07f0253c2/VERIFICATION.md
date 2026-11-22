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

# Reproducibility and limitations

Run `python checker.py` using Python 3 and SymPy. On the bundled checker, this prints:

`PASS: symbolic Fisher determinant and derivative; 4000 numerical local-optimum comparisons; rare-mixture asymptotics`

The checker constructs the \((A,p)\) Poisson Fisher matrix, checks its determinant symbolically, checks the transformed stationary polynomial and the strict positive cross-derivative with exact symbolic algebra, compares 4,000 seeded interior stationary points with nearby alternatives, and checks the three rare-mixture asymptotic regimes. The analytic proof in `RESULT.md`, not finite sampling, establishes global optimality and quantified limiting behavior.

The likelihood uses independent count samples; if one physical water sample is destructively split into coupled aliquots, the model must be changed. The result concerns a two-size-class, fixed-rate, fixed-sampling-effort local D criterion and is not experimentally validated. Independent audit is not performed.
