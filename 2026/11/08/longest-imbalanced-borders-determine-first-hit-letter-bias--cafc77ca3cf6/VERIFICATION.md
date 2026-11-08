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

The proof depends on the published exact first-hit bivariate generating function of Bóna, Maga and Richey (2026), followed by a variable change, justified integration of the normalized signed first-hit count, and a pointwise positive-polynomial bound on imbalanced borders.

Reproduce finite checks from this directory using `python3 checker.py`; no third-party packages are needed. It verifies 126 exact pattern generating-function series, 2,046 integral sign classifications, and eleven independent first-hit recurrence comparisons. The infinite-length assertion follows from the displayed proof rather than these tests. Numerical quadrature cannot independently certify all signs, and historical-priority review remains open. Independent audit: not performed.
