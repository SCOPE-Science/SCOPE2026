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

# Verification notes

The standalone `CHECK.py` uses exact symbolic differentiation of the stated ODE, reduces the predator nullcline to a concave quadratic, checks the original vector field at both positive rational-example equilibria, and verifies the Jacobian determinant and trace signs. Command: `python CHECK.py` (SymPy required).

The fully general theorem is proved by the analytic quadratic root classification and Jacobian inequalities in `RESULT.md`. The script does not establish the theorem by finite enumeration or assert PDE, global basin, or stochastic conclusions. Historical priority was compared against the originating full HTML preprint and accessible parts of several relevant older studies; a few older full texts could not be inspected. This work has not undergone independent scientific audit.
