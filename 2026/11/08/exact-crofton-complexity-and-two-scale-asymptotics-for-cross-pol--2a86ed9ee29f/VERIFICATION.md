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

The independent audit has not been performed. All statements below describe direct analytical checks and a finite numerical consistency test, not external certification.

Run `python check.py` from the package root using Python 3 and its standard library. The program integrates Gaussian order-statistic survival functions by Simpson quadrature and compares the resulting complete probability masses in dimensions 3, 4, 6 with a separately implemented geometric edge-crossing enumeration using 30,000 weighted random hyperplanes per dimension. It also checks the exact first-moment identity derived independently by summing edge projected lengths, and the dimension-three exact trigonometric value.

Expected terminal marker: `CROSSPOLYTOPE_CROFTON_FINITE_LAW_OK`.

Finite validation has no power to certify the \(d\to\infty\) beta limit, quadratic rare tail, moment convergence, or novelty. Those conclusions are supported, respectively, by Gaussian order-statistic asymptotics, empirical-quantile convergence, and dominated convergence in the written proof. The quadrature cutoff at 10 and numerical tolerances are explicit in `check.py`. The historical-priority comparison cannot exclude uncatalogued results.
