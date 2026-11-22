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

The analytic proof is self-contained in `RESULT.md`. Execute `python3 CHECK.py` with the Python standard library. The checker was run successfully with 95 assertions: numerical Feynman–Kac ODE independently compared with the closed transform; exact normalization and fluctuation-reflection identities; finite-time first and second cumulant comparisons; a separate OU covariance quadrature; effective-diffusivity sensitivity; and a seeded stochastic mixture experiment with 18,000 realizations.

The finite numerical experiments are finite checks, not proofs of laws for all parameters or all times. The process-law invariance follows exactly from the stochastic integral sign-gauge argument and independence; the transform follows by Feynman–Kac and stationary Gaussian integration; and the long-time limit follows from an explicit positive leading hyperbolic term. The public classification identifies a self-review only. No independent audit or independent validation has been performed.
