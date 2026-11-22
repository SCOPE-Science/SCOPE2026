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

# Verification

Run `python verify.py` with Python 3 and SymPy. This reconstructs the Lyapunov Gramian by solving all nine equations, verifies the full symbolic determinant against the Cauchy formula, proves stationary-polynomial and derivative identities by exact simplification, and checks the asymptotic coefficient with symbolic limits. Six numerical stationary roots are diagnostic only. The exact determinant and polynomial sign proof in `RESULT.md` establish the infinite-parameter conclusions. This self-review is not an independent audit.
