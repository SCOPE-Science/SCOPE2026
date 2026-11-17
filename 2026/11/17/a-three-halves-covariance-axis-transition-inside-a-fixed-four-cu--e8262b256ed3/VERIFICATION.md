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

# Verification of the covariance-axis transition

The supplied `artifacts/verify.py` uses Python 3, NumPy, SciPy, and SymPy. Run `python artifacts/verify.py` with the provided artifact in its own relative package path.

The checker creates exact section vertices by intersecting the plane with all edges of the four-cube; it triangulates their hull, and then computes simplex determinants and all three quadratic forms as exact rational numbers. It checks 15 rational parameter values from \(t=1\) through \(t=17\), including \(t=3/2\) and \(t=2\). The program also independently evaluates the symbolic fiber integrals and rational eigenvalue differences. The successful output recorded from this file was:

`FOUR_CUBE_PAIR_SECTION_CHECKS_PASSED profiles=15 vertices=118 tetrahedra=176`

Floating-point routines identify hull triangles, but the quantities compared are exact rational second moments; this method would not by itself prove correctness at every real parameter. The all-parameter claim instead follows from the explicit analytic integration and sign factorizations in RESULT.md. The code carries no claim of independent mathematical audit.
