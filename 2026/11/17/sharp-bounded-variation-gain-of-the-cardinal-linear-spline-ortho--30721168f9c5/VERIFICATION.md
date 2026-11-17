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

# Reproducible scientific verification

Execute `python verify.py` in the directory containing the seven embedded files (Python 3 and SymPy 1.10+ required). The checker symbolically verifies the infinite-grid inverse-Gram recurrence, explicit knot-response coefficient equations and exact three-part jump-profile identities. It separately computes finite-interval Galerkin systems with rational arithmetic at seven jump phases and three mesh radii, and verifies 119 algebraic moment equations on seventeen nodes. An observed complete run produced:

```
EXACT_GREEN_RECURRENCE_AND_PIECEWISE_STEP_PROFILE_PASS
INDEPENDENT_RATIONAL_FINITE_GRAM_APPROXIMATIONS_PASS 21
EXACT_STEP_MOMENT_EQUATIONS_AND_MAXIMUM_PASS 119
ALL_CARDINAL_SPLINE_BV_CHECKS_PASS
```

The unrestricted proof is in `RESULT.md`: finite tests cannot establish the theorem by extrapolation. Checks do not settle historical novelty or variants for nonuniform grids. This is not an independently audited mathematical result.
