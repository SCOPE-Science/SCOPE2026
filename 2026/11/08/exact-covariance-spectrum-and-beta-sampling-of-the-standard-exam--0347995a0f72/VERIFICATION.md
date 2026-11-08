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

# Reproducibility

The analytical derivation is in `RESULT.md`. Run `python3 checker.py` (Python 3 standard library only). It independently enumerates every ordering simplex satisfying the exact standard-example inequalities for n=2,3,4, and uses exact fractional order-statistic moments for the polytope volume, the two coordinate means, four covariance orbit types, and four diagonalization formulas. The valid ordering-simplex counts are 6, 48 and 720, a total of 774. Expected success marker: `STANDARD_EXAMPLE_EXACT_CHECKS_PASSED 774 3`.

The checker was executed from its supplied file and passed. It is a finite test, not a proof of any statement for arbitrary n. The infinite family is proved by beta disintegration and rational symbolic simplification in `RESULT.md`; no independent mathematical audit has been performed.
