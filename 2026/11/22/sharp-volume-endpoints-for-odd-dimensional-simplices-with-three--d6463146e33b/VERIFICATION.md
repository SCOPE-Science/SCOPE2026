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

The proof in `RESULT.md` establishes the general all-parameter result by constrained spectral optimization, a second-variation extremality test, and balanced-sign equality analysis. This is the decisive evidence; finitely many tests do not constitute an infinite proof.

The companion `centered_simplex_checker.py` was executed with Python 3. It completed 18 rational Gram-matrix calculations at dimensions \(5,7,9\), deformation ratios \(1/2,2/3,3/4\) and both extremal families. For each calculation it checked exact unit vertex squared norms, equal inverse-facet squared norms, the predicted squared inradius, and the squared Euclidean simplex volume by a full determinant. All checks passed.

No Lean formalization or independently performed mathematical audit is asserted. Unindexed historical work remains a priority risk.
