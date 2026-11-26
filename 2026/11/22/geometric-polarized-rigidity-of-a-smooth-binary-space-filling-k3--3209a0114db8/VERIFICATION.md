---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

The accompanying `check_polarized_aut.py` uses Python 3 and SymPy. It evaluates the homogeneous quartic over characteristic two, then checks: (1) four full Jacobian-chart ideals with unit Gröbner basis; (2) all six row-echelon Grassmannian cell equations and their reduced bases, certifying the geometric line points; (3) the five-line incidence graph; (4) all four graph-automorphism linear solution spaces in sixteen matrix coordinates; (5) the singularity of the path-reversal candidates and failure of polynomial preservation for the sole other invertible candidate.

The line-scheme reducedness argument in `RESULT.md` uses the full tangent spaces, not reducedness of the cell intersections. The remaining geometric and scheme-theoretic conclusions follow from exact algebraic ideals and linear systems that remain valid after extension of the base field, not from testing finitely many ground-field projectivities. The result does not classify unpolarized K3 automorphisms. Historical priority remains subject to unindexed literature.
