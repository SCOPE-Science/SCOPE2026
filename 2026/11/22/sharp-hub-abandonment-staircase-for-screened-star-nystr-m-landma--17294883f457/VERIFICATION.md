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

The all-parameter mathematical evidence is the block-inverse and determinant proof in RESULT.md. The standalone verifier is `verify.py`, which imports only SymPy and Python standard-library modules. Run `python verify.py` in this directory. It exercises symbolic equalities and exact-rational matrices and exhaustive small-star set comparisons; it does not treat finite enumeration as an infinite proof.

Observed local result: `PASS: 3557 exact symbolic, subset, and matrix assertions`.

Coverage: \(m=2,\ldots,12\) for explicit kernels and seven rational screening shifts, all budgets; \(m=2,\ldots,8\) for exhaustive subset checks at three shifts. Boundary \(k=m\), singleton \(k=1\), zero residual at full selection, and analytic tie conditions are addressed in the proof. Unproved extensions to weighted stars, other graphs and approximate kernels are excluded. Independent audit has not been performed.
