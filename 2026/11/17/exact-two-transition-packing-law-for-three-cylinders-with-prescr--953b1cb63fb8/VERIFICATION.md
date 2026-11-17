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

# Verification of the conical three-cylinder law

Run `python3 verify.py` using only the Python standard library. The verifier independently reconstructs three unit direction vectors and their mutual cross-product normals, numerically minimizes the signed dual one-dimensional objective using a golden-section procedure, and compares its output with the closed expression. It checks both unit-circle primal witnesses, their orthogonality constraints, the three line distances and sign-branch ordering at 1001 interior cone parameters. It also checks the derived critical parameter and orthogonal-axis radius.

Observed on the supplied script: `PASS 1001 cone values: dual minimizer, explicit primal configurations, signs, contacts, and transitions`.

The script uses floating-point tolerances and finite samples. The universal assertion, all transition values and exact identities are established by the analytical argument in `RESULT.md`, not by these tests. There has been no independent external audit.
