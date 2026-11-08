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

# Verification of the sharp Grassmann fourth-moment theorem

`CHECK.py` uses only the Python standard library and performs independent exact rational beta and Dirichlet moment calculations. Run with `python CHECK.py`. It establishes the two-probe fourth-moment identities against the closed invariant coefficient formulas in 120 even-dimensional rank pairs with dimensions from four through twenty-two. It additionally samples rational trace-free spectra for the two-sided spectral ratio bounds and tests the coefficient-sign transition.

The decisive universal arguments are the invariant-polynomial reduction, the two-probe conditional moment formulas, and the Lagrange-multiplier spectral extremization proof in `RESULT.md`. Finite checks do not verify the complete theorem independently. The upper equality classification requires the strict three-root Hessian argument; the lower equality classification requires even dimension. No separate independent audit has been performed.
