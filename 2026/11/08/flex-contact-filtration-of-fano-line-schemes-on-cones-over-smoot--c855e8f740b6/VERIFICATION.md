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

# Verification of contact-filtration calculations

The executable `artifacts/verify_cone.py` uses Python 3 and SymPy. It checks exact polynomial identities in local tangent-jet models for contact orders \(2\) through \(10\), computes the lengths \(\sum_{j=2}^{r-1}(r-j)\), verifies the full Fermat Hessian determinant for degrees \(3\) through \(9\), and cross-checks the first-layer Riemann–Roch expression for the Plücker Hilbert polynomial. Its recorded stdout is in `artifacts/verify_output.txt`, ending `ALL_CHECKS_PASSED`.

The proof of global validity for every smooth complex plane curve lies in `RESULT.md`: exact defining equations, formal contact expansions, global normal/conormal bundle and the Hessian inflection divisor. The finitely many executable cases are symbolic regression tests, not exhaustive checks of all curves or evidence of absolute novelty. No independent mathematical audit or formal proof certification was performed.
