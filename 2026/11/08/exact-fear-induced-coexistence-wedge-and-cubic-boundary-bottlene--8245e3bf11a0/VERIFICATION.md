---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify.py` with SymPy. Success prints `PHYSICAL_FOLD_ALGEBRA_OK`. The checks concern the normalized nullcline equation, its stationary branches, the exact fold width and expansion, the critical-boundary quadratic term and the algebraic two-equilibrium witness. The analytical proof in `RESULT.md` proves the physical range, uniqueness of the admissible fold, the complete count, and the stability of its branches. These computations do not constitute formal proof certification.
