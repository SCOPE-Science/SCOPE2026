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

The standalone `checker.py` runs under Python 3 standard library and checks the explicit non-equilateral example: total-circulation relation, vanishing weighted first and real quadratic moments, complex Gröbli equations for all three indices, exact image-induced center velocity and its expansion at four shrinking scales. Execution completed with `VERIFY_OK profile_equations=3 conserved_moments=3 image_drifts=4`.

The analytic proof establishes cancellation of the dipole, bounds the cubic Taylor remainder by the third power of the collapsing diameter, uses the exact pre-existing shape estimate, integrates the quadrupole term, and derives the limsup/liminf by unbounded logarithmic phase. Finite checks do not certify these infinite-time claims. Independent audit and definitive literature priority assessment have not been performed.
