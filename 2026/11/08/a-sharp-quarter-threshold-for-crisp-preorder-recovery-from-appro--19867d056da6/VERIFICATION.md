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

# Reproduction and proof boundaries

Run `python checker.py` using a standard Python 3 interpreter. The program uses only the Python standard library and exact integer arithmetic. A successful execution prints `QUANTITATIVE_S4_ALL_CHECKS_OK` following these checks:

- All \(5\) one-world and \(625\) two-world accessibility matrices on the five-level rational grid are compared with exhaustive valuations of both modal variables for the three axiom deficits; all crisp preorders on those carriers are checked for the global lower distance inequality and the strict-quarter equality.
- Another \(60\) seeded three-world frames are verified against every grid-valued valuation; \(350\) seeded one-eighth-grid perturbations of three-world crisp preorders are compared against every one of the \(29\) crisp preorders on three labelled worlds.
- The explicit three-world threshold example is checked to have defect \(1/4\) and nearest-preorder distance \(3/4\).

Proof ingredients requiring mathematical scrutiny beyond finite testing are the normality scalar inequality, the residuated box-composition law, and the exact threshold rounding implication. These are proved in `RESULT.md`. Finite experiments do not establish the theorem for arbitrary carrier sizes or the real interval. External independent validation has not been performed.
