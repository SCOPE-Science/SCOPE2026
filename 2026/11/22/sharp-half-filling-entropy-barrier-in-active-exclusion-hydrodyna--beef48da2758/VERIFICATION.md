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

# Reproducible verification

Run `python CHECKER.py` in an environment with Python, NumPy, and SymPy. The checked symbolic matrix identities are the exact Hessian/flux cancellation, existence of the entropy flux, the zero-density curvature normalization, the half-filling nilpotent Jacobian, and uniqueness of the Hessian ratio within the specified quadratic-polarization class. A Fourier-spectral PDE evaluation at 24 low-density physical trigonometric profiles and four activity strengths per profile tests the integrated infinitesimal balance against direct dissipation, along with its conditional decay inequality. The checker reports 83 assertion groups.

The universal no-pattern statement and the all-length/all-activity exponential estimate follow from the displayed symbolic identity, strict convexity, periodic Poincaré inequality, and the zero-dissipation argument in `RESULT.md`. Numerical testing does not establish the universal result. At densities above half filling the entropy production integrand can have either sign; no global energy decay is asserted there.

No independent audit, formal proof assistant, or experimental validation has occurred.
