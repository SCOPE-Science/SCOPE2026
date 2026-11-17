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

Run `python check.py` with SymPy installed. The checker uses exact integer/rational arithmetic, not numerical root plots or time integration. It reconstructs both equilibrium nullclines, the quartic and its four real-root brackets, Jacobian trace/determinant and discriminant, and tests the source–saddle–sink signs on each isolating interval by the rational midpoint derivative bound. It separately confirms two cooperative equilibria and the unique neutral equilibrium. This is finite algebraic verification; the uniform bounds follow from the mathematical proof using monotonicity, convexity, Rolle's theorem and a nonsingular-persistence argument. The calculations do not certify independent validation or general global dynamics.
