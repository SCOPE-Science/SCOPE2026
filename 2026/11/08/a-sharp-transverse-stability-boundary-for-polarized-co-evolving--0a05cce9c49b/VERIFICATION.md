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

Execute `python verify.py` in a Python environment with SymPy, NumPy, and SciPy. The script checks symbolic stationarity, exact longitudinal and transverse Jacobian blocks, exact transverse determinant, a resonance identity, 120 randomly constructed signed-eigenvector stochastic networks against their scalar reductions over a finite time interval, and two scalar long-time examples. Its numerical tolerances are specified in the code. Long-time full-system numerical integrations in a transversely unstable setting can depart from an analytically invariant symmetry manifold due to roundoff; this is expected and is not evidence against exact invariance.

The proof of the all-parameter stability threshold and convergence uses direct algebra and analytic inequalities in `RESULT.md`; finite simulations cannot establish those universal statements. The critical equality is only identified as linearly nonhyperbolic. No independent audit or independent validation has occurred.
