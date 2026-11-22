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

# Reproduction checks

Run `python verify.py` with NumPy and SciPy installed. The program checks exact sign-eigenvector invariance and reduced derivatives using rational arithmetic, compares finite-horizon trajectories of the complete and reduced systems on randomly generated directed two-community matrices with equal cross-group row mass, and checks the critical branch and large-time subcritical scaling numerically.

The differential equations, parameter ranges, phase classification, and non-numerical asymptotic proof are specified in `RESULT.md`. Finite computational checks are supplemental: their passing does not prove the universal or infinite-time quantifiers. Off-manifold stability, empirical interpretation and independent external validation have not been established.
