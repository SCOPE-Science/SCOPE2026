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

## Analytic checks

The proof establishes endpoint behavior, both unique elasticity crossings, the sharp rated-speed location criterion, and the necessary-and-sufficient level-set topology. An elementary exchange inequality verifies global optimality and uniqueness for any positive wind-speed density, not only the displayed example. Exact rational bounds on \(e\) certify a threshold for which four distinct crossings occur.

## Reproduction

Run `python CHECK.py` using Python 3 (standard library only). The script checks monotone-branch crossing locations, elementary antiderivative values, comparison with a single cut-in rule, and 20,001 extra grid values. Numerical grids and floating-point calculations serve only as supplementary regression tests; the analytical proof covers the universal assertion.

## Scope

The risk curve is a positive mathematical proxy, not a fitted mortality distribution. A 2016 predecessor's public summary was inspected, but its complete report was inaccessible during the comparison. Historical priority and real-world applicability remain provisional. No independent audit was performed.
