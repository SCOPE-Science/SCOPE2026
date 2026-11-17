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
# Reproduction of the finite classification

Run `python3 checker.py` alongside `cycles.csv` under Python 3. No nonstandard packages are needed. All computed values are integers or exact rational fractions. Each of 4096 three-step branches is solved by exact inversion of its affine fixed equation after checking that its trace is not two. The checker then imposes every time-ordered branch and modular-carry inequality, including fold equalities. The resulting admissible incidence distribution is 97 single occurrences, two eightfold occurrences and one 64-fold occurrence, giving 100 distinct periodic points. Exactly 96 of these are primitive three-periodic; their canonical 32 representative coordinates and return traces are independently listed in `cycles.csv` and compared against the recomputation.

The checker verifies that all primitive cycles avoid switching coordinates, so the traces belong to classical differentiable monodromy matrices. The complete return-trace census is 16 cycles of trace \(102\), eight of trace \(-34\) and eight of trace \(-98\), with determinant one. All are hyperbolic. It additionally checks 28 points on the mesh-\(1/18\) grid, 76 on the mesh-\(1/50\) grid and the exact overlap of four fixed points. Direct pointwise re-evaluation of the original nonlinear fractional-part map is performed.

No infinite-time or global dynamical assertion follows from this finite branch census. Full-period-four and period-two structures in the literature are not recomputed or independently reviewed here. Independent mathematical audit has not been performed.
