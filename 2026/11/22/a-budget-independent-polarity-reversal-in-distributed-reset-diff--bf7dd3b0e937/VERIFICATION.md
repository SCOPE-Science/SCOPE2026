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

# Mathematical verification

The provided `CHECK.py` runs with Python 3 standard library alone, reproduces the explicit Brownian Robin discounted transform, checks both inhomogeneous boundary conditions, the associated interior equation, distributed-reset averaging, the derivative numerator against finite differences, numerical optimizer globality on finite grids, and the exact sign transition in the two-point example for multiple positive resource budgets. A direct run produced: `PASS 11430 deterministic finite checks; critical k=4.812118250596; rL^2/D=23.156482057719`.

The uncountable family of reset distributions, strict uniqueness of the global optimizer, and unique positive crossover follow from the analytic inequalities and hyperbolic-sine ratio monotonicity in `RESULT.md`; finite assertions are consistency checks only. Published forward relations and the competing-risk point-source equivalence are acknowledged as prior mathematics. Independent validation has not been performed.
