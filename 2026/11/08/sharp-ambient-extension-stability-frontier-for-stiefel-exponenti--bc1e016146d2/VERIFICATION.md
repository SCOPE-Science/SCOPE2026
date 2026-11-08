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

The direct symbolic verification in `verify.py` checks the exact two-variable Jacobian, the characteristic polynomial, the determinant and the third memory-mode multiplier. The numerical differential checks evaluate the actual normalized-retraction recursion at the fixed point for selected \(\theta,c,t\), agreeing with the exact Jacobian to finite-difference precision. The proof of the infinite-time assertion uses discrete Lyapunov inequalities rather than finite simulation. No external independent audit has been carried out. The equality at the sharp threshold, global nonlinear stability and stochastic perturbations remain unresolved by this finding.
