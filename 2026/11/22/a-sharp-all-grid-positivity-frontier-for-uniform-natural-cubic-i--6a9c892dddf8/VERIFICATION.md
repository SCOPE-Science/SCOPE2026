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

# Reproduction

Run `python verify.py` using Python 3 and SymPy. The verifier independently constructs finite natural-spline cardinal coefficients by exact inversion of the tridiagonal curvature matrix. It checks 315 exact rational evaluation points against the closed negative-mass formula and symbolically checks nine nonnegative Bernstein coefficients as well as two sharp-constant identities. The analytic proof in `RESULT.md`, particularly its explicit Bernstein positivity certificate, establishes the all-grid statement; numerical or finite symbolic examples alone would not. Literature comparisons establish provisional best-knowledge priority only. There is no independent proof audit or external certification.
