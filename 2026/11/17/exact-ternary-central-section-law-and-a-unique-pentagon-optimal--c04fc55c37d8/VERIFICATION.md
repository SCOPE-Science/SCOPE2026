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

# Reproducibility and scope of checks

The proof in `RESULT.md` gives all-height analytic arguments. The companion file `verify_prism.py` is an executable corroboration with no dataset or hidden dependency other than Python 3 and SciPy.

The verifier independently counts crossings among all nine prism edges for exact-algebraic test normals, using rational coefficients of \(\sqrt3\), and compares that result with the proposed four-threshold classification. It samples integer normal coordinates from \(-7\) through \(7\) across six rational heights and skips degeneracies where a plane passes exactly through a vertex or a threshold. It also evaluates the two derived angular probability integrals with adaptive quadrature at eleven positive heights and independently locates the unique stationary height numerically. Its output after execution was:

`PASS: 40263 exact sign-cell / quadrature / extremizer checks; h*= 0.61368817674533`

The exact sign tests are exhaustive only over the specified finite integer grids, not over all normals or real heights. The numerical quadratures and derivative evaluations are validation checks, not proof of the infinite statements. The analytic proof derives the formulas and uniqueness for every positive real height.
