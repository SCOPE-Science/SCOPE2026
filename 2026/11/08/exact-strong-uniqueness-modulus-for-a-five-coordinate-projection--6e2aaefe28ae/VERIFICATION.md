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

# Verification of the sharp error bound

Execute `python verify.py` with SymPy. The executable checks, in rational arithmetic, the displayed basis and the minimum projection, the five active row norms, the positive weighted supporting-form identity, ranks of the equality constraints and supporting-form map, all seven uniquely defined simplex vertices, their exact operator norms, and a specific nonzero perturbation attaining the inequality. The checker uses no floating-point criterion for any mathematical assertion.

The universal claim follows from the analytical supporting-hyperplane and simplex argument in `RESULT.md`; finite exact checks alone cannot prove it without that argument. The scope is the real five-dimensional coordinate cube and its stated two-plane. No independent mathematical audit has been performed.
