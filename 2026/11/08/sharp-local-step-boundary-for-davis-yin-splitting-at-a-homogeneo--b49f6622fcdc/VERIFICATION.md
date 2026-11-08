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

# Verification and limits

Run `python VERIFY.py` with NumPy and SymPy installed. The script performs 1,208 assertions, including exact symbolic identities for the transverse multiplier and phase quadratic, an exact three-vertex path example, and direct centered finite-difference checks of the nonlinear iteration's Jacobian on several deterministic connected graphs, shifts, interaction strengths and step choices on either side of the calculated threshold.

The exact argument in RESULT.md, not these finite tests, establishes the theorem for every finite connected undirected weighted graph and all admissible positive parameters. The script tests selected graph families only; it neither establishes an infinite theorem from enumeration nor resolves neutral-step nonlinear dynamics. At the exact critical step, the derivative has \(-1\) eigenvalues, but the higher-order discrete dynamics has not been classified. No tests of variable timesteps, nonconstant potentials, weighted mass matrices or DYS II are claimed.
