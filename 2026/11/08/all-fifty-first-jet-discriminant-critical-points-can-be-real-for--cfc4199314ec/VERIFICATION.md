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

# Reproducibility and scope

Execute `python verify_ternary_jet.py` from a directory containing that file, with a standard Python 3 installation with SymPy. The program uses exact rational and symbolic arithmetic and prints `VERIFY_OK: N/gradients, 30 simple finite points, 6 two-point splittings, 8 pole points; total 50` upon success. It checks the meridian restriction using polynomial reduction modulo the unit-circle equation, derivative identities, finite-point Hessians, the two-branch perturbation derivatives, and both pole Taylor expansions and Hessians.

The symbolic checker does not directly quantify an explicit range of positive parameters or replace the implicit-function theorem. The analytic local persistence follows because each displayed limiting Hessian is invertible; finitely many neighborhoods allow a common sufficiently small positive parameter. The generic complex upper count is taken from Kozhasov–Mourrain–Parusiński (2026), Theorem 1.2, and has not been independently recomputed. No independent external mathematical audit has been performed.
