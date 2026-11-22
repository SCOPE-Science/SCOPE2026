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

The accompanying `check_polarized_aut.py` was executed using Python 3 and SymPy. It evaluates the homogeneous quartic over characteristic two, then checks: (1) four full Jacobian-chart ideals with unit Gröbner basis; (2) all six row-reduced Grassmannian chart equations and their reduced bases; (3) the five-line incidence graph; (4) all four graph-automorphism linear solution spaces in sixteen matrix coordinates; (5) the singularity of the path-reversal candidates and failure of polynomial preservation for the sole other invertible candidate.

The geometric and scheme-theoretic conclusions follow from exhaustive algebraic ideals and linear systems that remain valid after extension of the base field, not from testing finitely many ground-field projectivities. No formal proof assistant or independent audit has been used. The result does not classify unpolarized K3 automorphisms. Scientific novelty remains subject to priority comparison with unindexed literature.
