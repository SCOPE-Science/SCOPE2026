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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3 with SymPy. This is a standalone script containing the complete eight-state matrix construction and all enumeration logic.

It performs three distinct checks:

- Symbolically evaluates the scaled eight-state characteristic polynomial and checks its constant, first, and second coefficients in the variable \(y\), confirming the exact formulas used in the proof and polynomiality in \(y\).
- Runs a direct min-plus transfer calculation of minimum frustrated bonds and the number attaining it for 28 odd sizes through \(n=81\), comparing each with the closed-form formula.
- Independently enumerates every spin assignment using explicit graph edges for \(n=5,7,9\), without reusing the transfer-state recurrence.

The observed result was `VERIFY_OK symbolic_determinant=1 exact_transfer_sizes=28 exhaustive_spin_sizes=3`. All checks were performed on the standalone source included with the finding. The all-size proof is the analytic pentagon-bound and formal-determinant coefficient argument; finite enumerations are cross-checks, not an infinite certificate. Scientific priority is not formally certified by computation or by the bibliography search.
